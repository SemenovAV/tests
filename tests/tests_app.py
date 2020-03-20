import sys
import unittest
from io import StringIO
from unittest.mock import patch

import app


class TestsApp(unittest.TestCase):
    def setUp(self):
        self.dirs, self.docs = app.update_date()
        with patch('app.update_date', return_value=(self.dirs, self.docs)):
            with patch('app.input', return_value='q'):
                app.secretary_program_start()

    def test_delete(self):
        before_len = len(app.documents)
        with patch('app.input', return_value='10006'):
            app.delete_doc()
            self.assertLess(len(app.documents), before_len)

    def test_check_document_existance(self):
        self.assertTrue(app.check_document_existance('11-2'))

    def test_get_doc_owner_name(self):
        with patch('app.input', return_value='10006'):
            self.assertEqual(app.get_doc_owner_name(), "Аристарх Павлов")

    def test_get_all_doc_owners_names(self):
        self.assertIsInstance(app.get_all_doc_owners_names(), set)

    def test_remove_doc_from_shelf(self):
        before_len = len(app.directories['2'])
        app.remove_doc_from_shelf('10006')
        self.assertLess(len(app.directories['2']), before_len)

    def test_add_new_shelf(self):
        before_len = len(app.directories)
        app.add_new_shelf(shelf_number=4)
        self.assertGreater(len(app.directories), before_len)

    def test_append_doc_to_shelf(self):
        before_len = len(app.directories['2'])
        app.append_doc_to_shelf('11-2', '2')
        self.assertGreater(len(app.directories['2']), before_len)

    def test_get_doc_shelf(self):
        with patch('app.input', return_value='10006'):
            self.assertEqual(app.get_doc_shelf(), '2')

    def test_move_doc_to_shelf(self):
        before_len = len(app.directories['3'])
        with patch('app.input', side_effect=['10006', '3']):
            app.move_doc_to_shelf()
            self.assertGreater(len(app.directories['3']), before_len)

    def test_show_document_info(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        doc = app.documents[2]
        app.show_document_info(doc)
        sys.stdout = sys.__stdout__
        str = '{} "{}" "{}"'.format(doc['type'], doc['number'], doc['name'])
        self.assertEqual(capturedOutput.getvalue().strip(), str.strip())

    def test_add_new_doc_for_documents(self):
        before_len = len(app.documents)
        doc_number = '2765'
        doc_type = 'passport'
        owner_name = 'Аристарх Павлов'
        shelf_number = '1'
        with patch('app.input', side_effect=[doc_number, doc_type, owner_name, shelf_number]):
            app.add_new_doc()
            self.assertGreater(len(app.documents), before_len)

    def test_add_new_doc_for_shelf(self):
        before_len = len(app.directories['1'])
        doc_number = '2765'
        doc_type = 'passport'
        owner_name = 'Аристарх Павлов'
        shelf_number = '1'
        with patch('app.input', side_effect=[doc_number, doc_type, owner_name, shelf_number]):
            app.add_new_doc()
            self.assertGreater(len(app.directories['1']), before_len)

    def test_add_new_doc_for_return(self):
        doc_number = '2765'
        doc_type = 'passport'
        owner_name = 'Аристарх Павлов'
        shelf_number = '1'
        with patch('app.input', side_effect=[doc_number, doc_type, owner_name , shelf_number]):
            self.assertEqual(app.add_new_doc(), shelf_number)


if __name__ == '__main__':
    unittest.main()
