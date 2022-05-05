import unittest
from app.models import Articles

class Test_Article(unittest.TestCase):
    ''''Define setup method'''
    def setUp(self):
       self.new_article=Articles(
            {},
            "nimrod musungu",
            "The quick brown fox jumped over the lazy dog",
            "Ba ba black ship, have you any wool, yes sir, yes sir three bags full",
            "https://audmainsurance.co.ke/assets/images/products/Vehicle-Insurance.jpg",
            "2022-04-12T11:13:51Z",
            "I have a new article"
                )
        
    def test_instance(self):
        '''Tests to check if the articles are instantiated correctly'''
        self.assertTrue(isinstance(self.new_article,Articles))