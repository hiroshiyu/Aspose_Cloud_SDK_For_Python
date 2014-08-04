__author__ = 'AssadMahmood'
import unittest
import asposecloud

from asposecloud.barcode import Builder
from asposecloud.barcode import Reader


class TestAsposeBarcode(unittest.TestCase):

    def setUp(self):
        asposecloud.AsposeApp.app_key = '8356c76c7412f32bb85ae7472e842da4'
        asposecloud.AsposeApp.app_sid = '8EB6E644-4A40-4B50-8012-135D1F8F7513'
        asposecloud.AsposeApp.output_path = './output/'
        asposecloud.Product.product_uri = 'http://test.aspose.com/v1.1/'

    def test_save_barcode(self):
        builder = Builder()
        response = builder.generate('Text to generate barcode', 'QR', 'png')
        self.assertEqual(response.status_code, 200)

    def test_read_barcode_local(self):
        reader = Reader('barcodeQR.png')
        response = reader.read_from_local_image('./data/barcodeQR.png', 'QR')
        self.assertEqual(list, type(response))

if __name__ == '__main__':
    unittest.main()