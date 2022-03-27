from pickle import dumps
from synonyms import aliases
from tagsCounter import get_tags_number
import tagInfoRepository

alias = 'ydx'
site_to_search = aliases.get(alias) or alias
dictionary = get_tags_number(site_to_search)
tagInfoRepository.create(site_to_search, dictionary)

tagInfoRepository.get_by_url(site_to_search)
