import unittest
from tests.tests_app import TestsApp
from tests.tests_translate_it import TestTranslate
loader = unittest.TestLoader()


loader.loadTestsFromTestCase(TestsApp)
loader.loadTestsFromTestCase(TestTranslate)
unittest.main(testLoader=loader, verbosity=2)





