import requests, pickle
from bs4 import BeautifulSoup

# We scrape the login page to get our login token then we log in as 'guest' user
session = requests.Session() 
login_url = 'https://ucilnica.fmf.uni-lj.si/login/index.php'
response = session.get(login_url)
soup = BeautifulSoup(response.text, 'lxml')
token = soup.find('input', {'name': 'logintoken'})['value']

credentials = {  # Default credentials used to login as guest user
    'username': 'guest',
    'password': 'guest',
    'logintoken': token
}
session.post(login_url, data=credentials)

# These are the URLs containing the reservations, subject to change (only valid for 2025/2026)
urls = {'https://ucilnica.fmf.uni-lj.si/mod/wiki/view.php?pageid=1329', 'https://ucilnica.fmf.uni-lj.si/mod/wiki/view.php?pageid=1325',
         'https://ucilnica.fmf.uni-lj.si/mod/wiki/view.php?pageid=1323', 'https://ucilnica.fmf.uni-lj.si/mod/wiki/view.php?pageid=1328',
           'https://ucilnica.fmf.uni-lj.si/mod/wiki/view.php?pageid=1324', 'https://ucilnica.fmf.uni-lj.si/mod/wiki/view.php?pageid=1254',
             'https://ucilnica.fmf.uni-lj.si/mod/wiki/view.php?pageid=1255', 'https://ucilnica.fmf.uni-lj.si/mod/wiki/view.php?pageid=1331'
}

# We scrape the URLs for each link to a reservation (as the reservation format is <name> <url> <points>)
data = set()
for url in urls:
    ucilnica = session.get(url)
    soup = BeautifulSoup(ucilnica.text, 'lxml')
    items = soup.select('li')

    for item in items:
        a_tag = item.find('a')
    
        if a_tag:
            a_tag.extract()

        text = item.get_text(' ', strip=True)

        if '(' not in text and ')' not in text or len(text) > 100:  # Sometimes there's filler text that isn't a reservation
            continue

        # Extracting the name of the problem is, in theory, easy
        # ...if people followed guidelines, but some people
        # prefer to omit 'T', don't leave empty spaces (or add them where they
        # are not supposed to) or use ',' to denote decimals instead of '.'.
        
        name = text.split('(')[0]
        
        if name[-1] == ' ':
            name = name[:-6]
        else:
            name = name[:-5]

        if name[-1] == ':':
            name = name[:-1]
        elif name[-2:] == ': ':
            name = name[:-2]
        elif name[-3:] == ' : ':
            name = name[:-3]
        
        if name[-1] == ' ':
            name = name[:-1]

        data.add(name)

with open('Reservations.pkl', 'wb') as r:  # Writing as binary so we can save the set as is (and not as string)
    pickle.dump(data, r)
