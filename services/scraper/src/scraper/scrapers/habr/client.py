import httpx
import bs4
from ..base import Scraper

class habrScraper(Scraper):
    
    def __init__(self, baseUrl) -> None:
        
        super().__init__()
    
    def scrape(self) -> list:
        return super().scrape()

r = httpx.get('https://career.habr.com/vacancies/1000167467')
print(r.text)
print(r.headers)