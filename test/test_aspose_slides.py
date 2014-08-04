__author__ = 'AssadMahmood'
import unittest
import asposecloud
import os.path

from asposecloud.storage import Folder
from asposecloud.slides import Converter


class TestAsposeSlides(unittest.TestCase):

    def setUp(self):
        asposecloud.AsposeApp.app_key = '8356c76c7412f32bb85ae7472e842da4'
        asposecloud.AsposeApp.app_sid = '8EB6E644-4A40-4B50-8012-135D1F8F7513'
        asposecloud.AsposeApp.output_path = './output/'
        asposecloud.Product.product_uri = 'http://test.aspose.com/v1.1/'

    def test_convert_storage_file(self):
        folder = Folder()
        response = folder.upload_file('./data/test_convert_slide.pptx')
        self.assertEqual(True, response)

        converter = Converter('test_convert_slide.pptx')
        converter.convert(1,'png')
        self.assertTrue(os.path.exists('./output/test_convert_slide_1.png'))

if __name__ == '__main__':
    unittest.main()