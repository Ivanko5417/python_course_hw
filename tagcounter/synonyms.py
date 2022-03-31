import yaml


def get_key_value(s):
    split_items = s.split(':')
    key = str(split_items[0])
    value = ':'.join(split_items[1:])
    return key.strip(), value.strip()


def get_aliases_from_yaml(text):
    return dict(map(get_key_value, str(text).split('\n')[:-1]))


def fetch_aliases():
    data = yaml.load(open("tagcounter/synonyms.yaml"), Loader=yaml.Loader)
    return get_aliases_from_yaml(yaml.dump(data))



