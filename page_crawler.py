import requests
from bs4 import BeautifulSoup


class Page_Crawler:
    def __init__(self, search_term, location):
        self.url = f'https://www.indeed.com/jobs?q={search_term}&l={location}%2C%20TX&fromage=1'

    def load_page(self):
        page_raw = requests.get(self.url)
        page = BeautifulSoup(page_raw.content, 'html.parser')
        return page
