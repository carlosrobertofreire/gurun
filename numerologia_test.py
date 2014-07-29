#!/usr/bin/env python
# coding=UTF-8

import unittest
from numerologia import analisar


class TestNumerologia(unittest.TestCase):

    def test_Numerologia(self):
        self.assertTrue(analisar(u'nomequalquer') is not None)

    def test_Numerologia_de_cfreire(self):
        analise = analisar(u'cfreire')
        self.assertEqual(analise.valor, 17)
        self.assertEqual(analise.resultado, 'EXCELENTE')

    def test_Numerologia_de_dilmarousseff(self):
        analise = analisar(u'dilma rousseff')
        self.assertEqual(analise.valor, 15)
        self.assertEqual(analise.resultado, 'PÉSSIMO')

    def test_Numerologia_de_carlos(self):
        analise = analisar(u'carlos')
        self.assertEqual(analise.valor, 10)
        self.assertEqual(analise.resultado, 'PÉSSIMO')

    def test_Numerologia_de_collor(self):
        analise = analisar(u'collor')
        self.assertEqual(analise.valor, 7)
        self.assertEqual(analise.resultado, 'EXCELENTE')

    def test_Numerologia_de_b(self):
        analise = analisar(u'b')
        self.assertEqual(analise.valor, 2)
        self.assertEqual(analise.resultado, 'BOM')

    def test_Numerologia_de_db(self):
        analise = analisar(u'db')
        self.assertEqual(analise.valor, 6)
        self.assertEqual(analise.resultado, 'RUIM')


if __name__ == '__main__':
    unittest.main()
