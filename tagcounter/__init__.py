import sys
from tagcounter.gui import GUI
from tagcounter.synonyms import aliases
from tagcounter.tagsCounter import get_tags_number
import tagcounter.tagInfoRepository as tagInfoRepository


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


def main():
    if len(sys.argv) <= 1:
        GUI(get, view)
    else:
        print('Console')


if __name__ == '__main__':
    main()