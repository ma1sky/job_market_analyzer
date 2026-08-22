from abc import ABC, abstractmethod


class Scraper(ABC):

    def __init__(self) -> None:
        self.baseUrl: str
        self.params: list[str]

    @abstractmethod
    def scrape(self) -> list:
        pass