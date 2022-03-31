import unittest
from tagcounter.synonyms import get_aliases_from_yaml

aliases_example = '''ydx: yandex.ru
ggl: google.com
fb: facebook.com
'''

aliases_example_duplicates = '''ydx: yandex.ru
ggl: google.com
fb: facebook.com
ggl: google.com
fb: facebook.com
'''


class MyTestCase(unittest.TestCase):
    def test_get_aliases_from_yaml(self):
        self.assertEqual(
            get_aliases_from_yaml(aliases_example),
            {'ydx': 'yandex.ru', 'ggl': 'google.com', 'fb': 'facebook.com'}
        )

    def test_get_aliases_from_yaml_duplicates(self):
        self.assertEqual(
            get_aliases_from_yaml(aliases_example_duplicates),
            {'ydx': 'yandex.ru', 'ggl': 'google.com', 'fb': 'facebook.com'}
        )

if __name__ == '__main__':
    unittest.main()
