import requests
from bs4 import BeautifulSoup
from .markdown import Markdown as md


class Wikipage:
    def __init__(self, title):
        self.title = title

    def __eq__(self, other):
        return self.title == other.title

    @property
    def abs_url(self):
        EN_WIKI = "https://en.wikipedia.org/wiki/"
        return EN_WIKI + self.rel_url

    @property
    def rel_url(self):
        return self.title.replace(" ", "_").replace("'", "%27")

    @property
    def exists(self):
        return self.title and not self.is_redlink

    @property
    def is_disambiguated(self):
        return self.exists and "(" in self.title

    @property
    def is_redlink(self):
        return "not exist" in self.title

    @property
    def soup(self):
        return BeautifulSoup(self.text, "html.parser")

    @property
    def subject(self):
        return self.title.split(" (")[0]

    @property
    def text(self):
        return requests.get(self.abs_url).text

    def to_link(self, alias=None):
        return md.a(self.title) if not alias else md.a(self.title, alias)
