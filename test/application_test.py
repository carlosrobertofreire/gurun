#!/usr/bin/env python
# coding=UTF-8

import os
import sys
topdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(topdir)
import unittest
from selenium import webdriver


class TestApplication(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_abrir_aplicacao(self):
        driver = self.driver
        driver.get("http://0.0.0.0:5000")
        self.assertEqual("Numerologia WS", driver.title)

    def test_analisar_cfreire(self):
        self.analisar("cfreire", u"EXCELENTE")

    def test_analisar_carlos(self):
        self.analisar("carlos", u"PÉSSIMO")

    def test_analisar_carlosroberto(self):
        self.analisar("carlos roberto", u"BOM")

    def test_analisar_db(self):
        self.analisar("db", u"RUIM")

    def tearDown(self):
        self.driver.close()

    def analisar(self, nome_esperado, resultado_esperado):
        driver = self.driver
        driver.get("http://0.0.0.0:5000")
        nome = driver.find_element_by_name("nome")
        nome.send_keys(nome_esperado)
        driver.find_element_by_css_selector("button[type=submit]").click()
        resultado = driver.find_element_by_id("resultado")
        self.assertEqual(resultado_esperado, resultado.text)


if __name__ == "__main__":
    unittest.main()
