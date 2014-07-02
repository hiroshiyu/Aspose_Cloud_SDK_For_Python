__author__ = 'AssadMahmood'
import requests

from asposecloud import AsposeApp
from asposecloud import Product
from asposecloud.common import Utils


class Converter:

    def __init__(self, filename):
        self.filename = filename

        if not filename:
            raise ValueError("filename not specified")

        self.base_uri = Product.product_uri + 'pdf/' + self.filename

    def convert(self, save_format, remote_folder='', storage_type='Aspose', storage_name=None):
        if not save_format:
            raise ValueError("save_format not specified")

        str_uri = self.base_uri + '?format=' + save_format
        str_uri = Utils.append_storage(str_uri, remote_folder, storage_type, storage_name)

        signed_uri = Utils.sign(str_uri)
        response = requests.get(signed_uri, headers={
            'content-type': 'application/json', 'accept': 'application/json'
        }, stream=True)

        save_format = 'zip' if save_format == 'html' else save_format
        output_path = AsposeApp.output_path + Utils.get_filename(self.filename) + '.' + save_format
        Utils.save_file(response, output_path)
        return output_path

    @staticmethod
    def convert_local_file(input_file, save_format):
        if not input_file:
            raise ValueError("input_file not specified")

        if not save_format:
            raise ValueError("save_format not specified")

        str_uri = Product.product_uri + 'pdf/convert?format=' + save_format

        signed_uri = Utils.sign(str_uri)
        response = Utils.upload_file_binary(input_file, signed_uri)

        save_format = 'zip' if save_format == 'html' else save_format
        output_path = AsposeApp.output_path + Utils.get_filename(input_file) + '.' + save_format
        Utils.save_file(response, output_path)
        return output_path
