#!/usr/bin/env python
#coding=utf-8

import bibtex
import unittest
class TestAuthorExtract(unittest.TestCase):
    def setUp(self):
        self.simple_author_1 = "Smith"
        self.simple_author_2 = "Jones"
        self.author_1 = "John Smith"
        self.author_2 = "Bob Jones"
        self.author_3 = "Justin Kenneth Pearson"
        self.surname_first_1 = "Pearson, Justin Kenneth"
        self.surname_first_2 = "Van Hentenryck, Pascal"
        self.multiple_authors_1 = "Pearson, Justin and Jones, Bob"

    def test_author_1(self):
        #Test only surnames.
        (Surname, FirstNames) = bibtex. extract_author(self.simple_author_1)
        self.assertEqual ( (Surname, FirstNames), ('Smith', '') )
        (Surname, FirstNames) = bibtex. extract_author(self.simple_author_2)
        self.assertEqual ( (Surname, FirstNames), ('Jones', '') )        

def main():
    print("Hello,world!")

if __name__ == "__main__":
    unittest.main() 