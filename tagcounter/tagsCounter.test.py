import unittest
from tagcounter.tagsCounter import HTMLTagCounter


site_example1 = '''
<!DOCTYPE html>
<html>
<body>

<h1>My First Heading</h1>

<p>My first paragraph.</p>

</body>
</html>
'''


class MyTestCase(unittest.TestCase):

    def test_get_tags_number(self):
        counter = HTMLTagCounter()

        counter.feed(site_example1)
        self.assertEqual(counter.tagsDictionary,  {'html': 1, 'body': 1, 'h1': 1, 'p': 1})

if __name__ == '__main__':
    unittest.main()
