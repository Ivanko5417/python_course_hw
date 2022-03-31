import sys
from tagcounter.logger import configure_logger
import logging
from tagcounter.gui import GUI
from tagcounter.console import Console
from tagcounter.synonyms import aliases
from tagcounter.tagsCounter import get_tags_number
import tagcounter.tagInfoRepository as tagInfoRepository


def get_url_by_alias(alias):
    aliased_url = aliases.get(alias)
    if aliased_url is not None:
        return aliased_url
    url = alias
    return url if url.startswith('http') else ('https://' + url)


def get(url_or_alias):
    url = get_url_by_alias(url_or_alias)
    configure_logger(url)
    dictionary = get_tags_number(url)
    logging.info(f'Result of getting data from web: [{dictionary}]')
    tagInfoRepository.create(url, dictionary)
    return dictionary


def view(url_or_alias):
    url = get_url_by_alias(url_or_alias)
    configure_logger(url)
    result = tagInfoRepository.get_by_url(url)
    logging.info(f'Result of getting data from db: result=[{result}]')
    return result



def main():
    if len(sys.argv) <= 1:
        GUI(get, view)
    else:
        Console(get, view)


if __name__ == '__main__':
    main()