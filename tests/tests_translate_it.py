import unittest
from unittest.mock import patch

from tools.translate import translate_it


class TestTranslate(unittest.TestCase):
  def setUp(self) -> None:
    self.translate = translate_it('hello', 'ru', 'en',
                                 'trnsl.1.1.20200320T192455Z.e88d9cc28ffbec7a.236ec3e7ef338619746bac73e024093588416e50')
  def test_code_200(self):
    self.assertEqual(200, self.translate['code'])

  def test_translate(self):
    self.assertEqual('привет', ''.join(self.translate['text']))
