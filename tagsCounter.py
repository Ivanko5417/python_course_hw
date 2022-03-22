import requests
from html.parser import HTMLParser


class HTMLTagCounter(HTMLParser):
    tagsDictionary = {}

    def feed(self, html_text):
        self.tagsDictionary = {}
        super(HTMLTagCounter, self).feed(html_text)
        self.tagsDictionary = dict(sorted(self.tagsDictionary.items(), key=lambda arr: arr[1], reverse=True))

    def handle_starttag(self, tag, attrs):
        self.tagsDictionary.setdefault(tag, 0)
        self.tagsDictionary[tag] = self.tagsDictionary.get(tag) + 1


def get_tags_number(url):
    response = requests.get(url)

    counter = HTMLTagCounter()
    counter.feed(response.text)
    return counter.tagsDictionary


print(get_tags_number('https://www.google.com/'))