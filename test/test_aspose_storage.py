__author__ = 'AssadMahmood'
import unittest
import asposecloud
import os.path

from asposecloud.storage import Folder
from asposecloud.common import Utils


class TestAsposeStorage(unittest.TestCase):

    def setUp(self):
        asposecloud.AsposeApp.app_key = '8356c76c7412f32bb85ae7472e842da4'
        asposecloud.AsposeApp.app_sid = '8EB6E644-4A40-4B50-8012-135D1F8F7513'
        asposecloud.AsposeApp.output_path = './output/'
        asposecloud.Product.product_uri = 'http://test.aspose.com/v1.1/'

    def test_get_files(self):
        fld = Folder()
        files = fld.get_files()
        assert(isinstance(files, list))

    def test_upload_file(self):
        fld = Folder()
        response = fld.upload_file('./data/test_uploadfile.docx')
        self.assertEqual(response, True)

    def test_get_file(self):
        fld = Folder()
        response = fld.get_file('test_uploadfile.docx')
        Utils.save_file(response, asposecloud.AsposeApp.output_path + 'test_uploadfile.docx')
        self.assertEqual(True, os.path.exists(asposecloud.AsposeApp.output_path + 'test_uploadfile.docx'))

if __name__ == '__main__':
    unittest.main()