from os import EX_PROTOCOL
import re
import requests
from bs4 import BeautifulSoup


class Page_Crawler:
    def __init__(self, search_term, location, exp, trim_start, trim_end):
        self.url = f'https://www.indeed.com/jobs?q={search_term}&l={location}%2C%20TX&fromage=1'
        self.exp = exp
        self.trim_start = trim_start
        self.trim_end = trim_end

    def load_page(self):
        page_raw = requests.get(self.url)
        page = BeautifulSoup(page_raw.content, 'html.parser')
        self.page = page

    # Return job count as an integer
    def parse_result(self):
        match = re.search(self.exp, str(self.page))
        count = int(match.group()[self.trim_start:-self.trim_end])
        return count

    # GETTERS / SETTERS
    def get_url(self):
        return self.url

    def set_url(self, search_term, location):
        self.url = f'https://www.indeed.com/jobs?q={search_term}&l={location}%2C%20TX&fromage=1'

    def get_expression(self):
        return self.exp

    def set_expression(self, exp):
        self.exp = exp

    def get_trim(self):
        return (self.trim_start, self.trim_end)

    def set_trim(self, trim_start, trim_end):
        self.trim_start = trim_start
        self.trim_end = trim_end
