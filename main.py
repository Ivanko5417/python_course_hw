from synonyms import aliases
from tagsCounter import get_tags_number

alias = 'ydx'
site_to_search = aliases.get(alias) or alias

print(get_tags_number(site_to_search))