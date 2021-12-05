import requests
from bs4 import BeautifulSoup


def load_page(url):
    page_raw = requests.get(url)
    page = BeautifulSoup(page_raw.content, 'html.parser')
    return page


# url = 'https://www.indeed.com/jobs?q=Python&l=Austin%2C%20TX&fromage=1&vjk=299205b85bc7fd35'


bs_page = load_page(
    'https://www.indeed.com/jobs?q=Python&l=Austin%2C%20TX&fromage=1&vjk=299205b85bc7fd35')
result = bs_page.find_all('div', id="searchCountPages")
print(result)
