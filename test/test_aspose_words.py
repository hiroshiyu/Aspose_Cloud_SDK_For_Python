__author__ = 'AssadMahmood'
import unittest
import asposecloud
import os.path

from asposecloud.words import Converter


class TestAsposeWords(unittest.TestCase):

    def setUp(self):
        asposecloud.AsposeApp.app_key = '8356c76c7412f32bb85ae7472e842da4'
        asposecloud.AsposeApp.app_sid = '8EB6E644-4A40-4B50-8012-135D1F8F7513'
        asposecloud.AsposeApp.output_path = './output/'
        asposecloud.Product.product_uri = 'http://test.aspose.com/v1.1/'

    def test_convert_local_file(self):
        # Create object of words converter class
        converter = Converter('file_on_storage.docx')
        converter.convert_local_file('./data/test_convertlocal.docx', 'doc')
        self.assertEqual(True, os.path.exists('./output/test_convertlocal.doc'))

if __name__ == '__main__':
    unittest.main()