import unittest

from tools.translate import translate_it


class TestTranslate(unittest.TestCase):

    def test_code_200(self):
        self.assertEqual(200, translate_it('hello', 'ru', 'en',
                                           'trnsl.1.1.20200320T192455Z.e88d9cc28ffbec7a.236ec3e7ef338619746bac73e024093588416e50')[
            'code'])

    def test_translate(self):
        self.assertEqual('привет', ''.join(translate_it('hello', 'ru', 'en',
                                                        'trnsl.1.1.20200320T192455Z.e88d9cc28ffbec7a.236ec3e7ef338619746bac73e024093588416e50')[
                                               'text']))

    def test_translate_error(self):
        self.assertEqual(501, translate_it('привет', 'rr', 'en','trnsl.1.1.20200320T192455Z.e88d9cc28ffbec7a.236ec3e7ef338619746bac73e024093588416e50')[
                                               'code'])
