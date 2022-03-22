import yaml
from yaml import Loader

data = yaml.load(open("./synonyms.yaml"), Loader=Loader)
fileText = yaml.dump(data)
withoutLast = slice(0, -1)

aliases = dict(map(lambda s: s.split(':'), str(fileText).split('\n')[withoutLast]))
print(aliases)


