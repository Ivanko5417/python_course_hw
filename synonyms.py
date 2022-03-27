import yaml
from yaml import Loader

data = yaml.load(open("./synonyms.yaml"), Loader=Loader)
fileText = yaml.dump(data)


def get_key_value(s):
    split_items = s.split(':')
    key = str(split_items[0])
    value = ':'.join(split_items[1:])
    return key.strip(), value.strip()


aliases = dict(map(get_key_value, str(fileText).split('\n')[:-1]))
print(aliases)


