import requests
from bs4 import BeautifulSoup


# login magic
session = requests.Session()  # idk how to work with objects, i just copied this from an article
login_url = 'https://ucilnica.fmf.uni-lj.si/login/index.php'
response = session.get(login_url)
soup = BeautifulSoup(response.text, 'lxml')
token = soup.find('input', {'name': 'logintoken'})['value']

credentials = {
    'username': 'guest',
    'password': 'guest',
    'logintoken': token
}
session.post(login_url, data=credentials)

# scraping part (urls are subject to change, sadly)
urls = {'https://ucilnica.fmf.uni-lj.si/mod/wiki/view.php?pageid=1329', 'https://ucilnica.fmf.uni-lj.si/mod/wiki/view.php?pageid=1325',
         'https://ucilnica.fmf.uni-lj.si/mod/wiki/view.php?pageid=1323', 'https://ucilnica.fmf.uni-lj.si/mod/wiki/view.php?pageid=1328',
           'https://ucilnica.fmf.uni-lj.si/mod/wiki/view.php?pageid=1324', 'https://ucilnica.fmf.uni-lj.si/mod/wiki/view.php?pageid=1254',
             'https://ucilnica.fmf.uni-lj.si/mod/wiki/view.php?pageid=1255', 'https://ucilnica.fmf.uni-lj.si/mod/wiki/view.php?pageid=1331'
}

links = set()
for url in urls:
    ucilnica = session.get(url)
    soup = BeautifulSoup(ucilnica.text, 'lxml')
    for link in soup.find_all('a'):
        new_link = link.get('href')
        new_link = str(new_link)
        new_link = new_link.split('/')
        if 'problems' in new_link:
            new_link = new_link[4].split('?')
            new_link = new_link[0].split('%')
            links.add(new_link[0])

reservations = open('Reservations.txt', 'w')
reservations.write(str(links))
reservations.close()