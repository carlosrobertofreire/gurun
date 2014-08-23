#!/usr/bin/env python
# coding=UTF-8

import os
import sys
topdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(topdir)
import unittest
from util import remover_acentos, remover_acentos_e_caracteres_especiais


class TestUtil(unittest.TestCase):

    def test_remover_acentos(self):
        s = u"João Olá É!"
        self.assertEqual(remover_acentos(s), "Joao Ola E!")


    def test_remover_acentos_e_caracteres_especiais(self):
        s = u"João Olá!#$@ Tudo bem"
        self.assertEqual(
            remover_acentos_e_caracteres_especiais(s),
            "Joao Ola Tudo bem"
        )

if __name__ == '__main__':
    unittest.main()
