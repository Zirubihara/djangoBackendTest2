import unittest

from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import CustomerList

#class TestStringMethods(unittest.TestCase):
class TestStringMethods(SimpleTestCase):

    def test_elo(self):
        url = reverse('list')
        print(resolve(url))
        self.assertEquals(resolve(url).func, CustomerList)

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()