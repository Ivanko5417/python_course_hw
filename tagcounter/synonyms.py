import yaml

data = yaml.load(open("tagcounter/synonyms.yaml"), Loader=yaml.Loader)
fileText = yaml.dump(data)


def get_key_value(s):
    split_items = s.split(':')
    key = str(split_items[0])
    value = ':'.join(split_items[1:])
    return key.strip(), value.strip()


aliases = dict(map(get_key_value, str(fileText).split('\n')[:-1]))
print(aliases)

