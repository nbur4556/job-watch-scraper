import requests
from bs4 import BeautifulSoup


def get_url(search_term, location):
    return f'https://www.indeed.com/jobs?q={search_term}&l={location}%2C%20TX&fromage=1'


def load_page(url):
    page_raw = requests.get(url)
    page = BeautifulSoup(page_raw.content, 'html.parser')
    return page


# Run Application
url = get_url('Javascript', 'Austin')
print(url)
bs_page = load_page(url)
result = bs_page.find_all('div', id="searchCountPages")
print(result)
