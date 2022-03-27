import sys
from gui import GUI
from synonyms import aliases
from tagsCounter import get_tags_number
import tagInfoRepository

if len(sys.argv) <= 1:
    print('GUI')
else:
    print('Console')


def get_url_by_alias(alias):
    return aliases.get(alias) or alias


def get(url_or_alias):
    url = get_url_by_alias(url_or_alias)
    dictionary = get_tags_number(url)
    tagInfoRepository.create(url, dictionary)
    return dictionary


def view(url_or_alias):
    url = get_url_by_alias(url_or_alias)
    return tagInfoRepository.get_by_url(url)


gui = GUI(get, view)
