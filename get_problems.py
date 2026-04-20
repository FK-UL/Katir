import requests, pickle
from bs4 import BeautifulSoup

data = {}  # We save the data in the format <problem_name>: <difficulty>
i = 1

while True:
    # Scrape each html page individually
    url = f'https://open.kattis.com/problems?page={i}'
    kattis = requests.get(url)
    soup = BeautifulSoup(kattis.text, 'lxml')
    changes_made = False
 
    rows = soup.select('tbody tr')

    for row in rows:  # We go by each 'row' i.e problem to get the name and difficulty
        name_tag = row.select_one('td a')
        name = name_tag.get_text(strip=True) if name_tag else None

        diff_tag = row.select_one('span.difficulty_number')
        difficulty = diff_tag.get_text(strip=True) if diff_tag else None

        if name and difficulty:
            try:
                data[name] = float(difficulty)
            except:  # To filter difficulty ranges (i.e difficulties in the format 'x.y - w.z').
                data[name] = float(difficulty[:3])  # As per the rules, the lower bound is taken.
            
            changes_made = True

    if changes_made == False:  # Pages out of range don't return 404
                               # instead they just contain no data
        break

    i += 1


with open('Problems.pkl', 'wb') as p:  # Writing as binary to be able to save as dict()
    pickle.dump(data, p)
