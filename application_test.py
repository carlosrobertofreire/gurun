#!/usr/bin/env python
# coding=UTF-8

import unittest
from selenium import webdriver


class TestApplication(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_abrir_aplicacao(self):
        driver = self.driver
        driver.get("http://0.0.0.0:5000")
        self.assertIn("Numerologia", driver.title)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
