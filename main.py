import unittest
from tests.tests_app import TestsApp
from tests.tests_translate_it import TestTranslate
from tests.selenium_tests import TestsYandexAuth
loader = unittest.TestLoader()


loader.loadTestsFromTestCase(TestsApp)
loader.loadTestsFromTestCase(TestTranslate)
loader.loadTestsFromTestCase(TestsYandexAuth)
unittest.main(testLoader=loader, verbosity=2)





