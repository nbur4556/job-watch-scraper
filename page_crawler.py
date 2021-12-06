import re
import requests
from bs4 import BeautifulSoup


class Page_Crawler:
    def __init__(self, search_term, location):
        self.url = f'https://www.indeed.com/jobs?q={search_term}&l={location}%2C%20TX&fromage=1'
        self.expression = r'([Pp]age\s1\sof\s[0-9]*\sjobs)'
        self.trim_start = 10
        self.trim_end = 5

    def load_page(self):
        page_raw = requests.get(self.url)
        page = BeautifulSoup(page_raw.content, 'html.parser')
        self.page = page

    # Return job count as an integer
    def parse_result(self):
        match = re.search(self.expression, str(self.page))
        count = int(match.group()[self.trim_start:-self.trim_end])
        return count
