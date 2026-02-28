import requests
from bs4 import BeautifulSoup


names = set()  # set to filter duplicates and for quick lookup
for i in range(1, 59):
    url = f'https://open.kattis.com/problems?page={i}' 
    # values >59 also return a response despite containing no problem data
    # this was the best i could do, probably will just manually update for now
    # when new tasks are added to kattis and the number of pages increases

    # ...probably can just add a check for a specific element on the empty pages to break the loop
    # too lazy to do that now, TODO in the future.
    kattis = requests.get(url)
    soup = BeautifulSoup(kattis.text, 'lxml')

    for url in soup.find_all('a'):
        new_url = url.get('href')
        new_url = str(new_url)
        new_url = new_url.split('/')

        if len(new_url) >= 3 and 'problems' in new_url:
            new_url = f'{new_url[2]}'
            names.add(new_url)

problems = open('Problems.txt', 'w')
problems.write(str(names))
problems.close()




