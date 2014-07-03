__author__ = 'AssadMahmood'
import requests
import os

from asposecloud import Product
from asposecloud.common import Utils


class Builder:
    def __init__(self):
        self.base_uri = Product.product_uri + 'barcode'

    def generate(self, code_text, symbology='QR', image_format='png', x_res=None, y_res=None, x_dim=None,
                 y_dim=None, remote_folder='', storage_type='Aspose', storage_name=None):
        if not code_text:
            raise ValueError("code_text not specified.")

        if symbology == '':
            raise ValueError("symbology can not be empty.")

        if image_format == '':
            raise ValueError("image_format can not be empty.")

        str_uri = self.base_uri + '/generate?text=' + code_text + '&type=' + symbology + '&format=' + image_format
        if x_res:
            str_uri += '&resolutionX=' + x_res
        if y_res:
            str_uri += '&resolutionY=' + y_res
        if x_dim:
            str_uri += '&dimensionX=' + x_dim
        if y_dim:
            str_uri += '&dimensionY=' + y_dim

        str_uri = Utils.append_storage(str_uri, remote_folder, storage_type, storage_name)

        signed_uri = Utils.sign(str_uri)
        response = requests.get(signed_uri, headers={
            'content-type': 'application/json', 'accept': 'application/json'
        }, stream=True)

        return response


class Reader:
    def __init__(self, filename):
        self.filename = filename

        if not filename:
            raise ValueError("filename not specified")

        self.base_uri = Product.product_uri + 'barcode'

    def read(self, symbology=None, remote_folder='', storage_type='Aspose', storage_name=None):
        str_uri = self.base_uri + '/' + self.filename + '/recognize'
        if symbology:
            str_uri += '?type=' + symbology

        str_uri = Utils.append_storage(str_uri, remote_folder, storage_type, storage_name)

        signed_uri = Utils.sign(str_uri)
        response = requests.get(signed_uri, headers={
            'content-type': 'application/json', 'accept': 'application/json'
        }).json()
        return response['Barcodes'] if response['Code'] == 200 else False

    @staticmethod
    def read_from_local_image(local_image, symbology):
        if not local_image:
            raise ValueError("local_image not specified")

        filename = os.path.basename(local_image)

        str_uri = Product.product_uri + 'storage/file/' + filename
        signed_uri = Utils.sign(str_uri)
        Utils.upload_file_binary(local_image, signed_uri)

        str_uri = Product.product_uri + 'barcode/' + filename + '/recognize'
        if symbology:
            str_uri += '?type=' + symbology

        signed_uri = Utils.sign(str_uri)
        response = requests.get(signed_uri, headers={
            'content-type': 'application/json', 'accept': 'application/json'
        }).json()
        return response['Barcodes'] if response['Code'] == 200 else False