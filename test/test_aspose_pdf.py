__author__ = 'AssadMahmood'
import unittest
import asposecloud
import os.path

from asposecloud.storage import Folder
from asposecloud.pdf import Converter
from asposecloud.pdf import TextEditor


class TestAsposePdf(unittest.TestCase):

    def setUp(self):
        asposecloud.AsposeApp.app_key = '8356c76c7412f32bb85ae7472e842da4'
        asposecloud.AsposeApp.app_sid = '8EB6E644-4A40-4B50-8012-135D1F8F7513'
        asposecloud.AsposeApp.output_path = './output/'
        asposecloud.Product.product_uri = 'http://test.aspose.com/v1.1/'

    def test_convert_local_file(self):
        # Create object of pdf converter class
        converter = Converter('file_on_storage.pdf')
        converter.convert_local_file('./data/test_convertlocal.pdf', 'doc')
        self.assertEqual(True, os.path.exists('./output/test_convertlocal.doc'))

    def test_convert_storage_file(self):
        folder = Folder()
        response = folder.upload_file('./data/test_file_on_storage.pdf')
        self.assertEqual(True, response)

        converter = Converter('test_file_on_storage.pdf')
        raised = False
        try:
            response = converter.convert('doc')
        except:
            raised = True
        self.assertFalse(raised)

    def test_replace_text(self):
        folder = Folder()
        response = folder.upload_file('./data/test_replace_text.pdf')
        self.assertEqual(True, response)

        editor = TextEditor('test_replace_text.pdf')
        raised = False
        try:
            response = editor.replace_text(1, 'Kevin', 'Nick', False)
        except:
            raised = True
        self.assertFalse(raised)

if __name__ == '__main__':
    unittest.main()