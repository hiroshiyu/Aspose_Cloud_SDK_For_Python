__author__ = 'AssadMahmood'
import os
import requests

from asposecloud import Product
from asposecloud.common import Utils


class Folder:

    def __init__(self):
        self.str_uri_folder = Product.product_uri + 'storage/folder/'
        self.str_uri_file = Product.product_uri + 'storage/file/'
        self.str_uri_exist = Product.product_uri + 'storage/exist/'
        self.str_uri_disc = Product.product_uri + 'storage/disc'

    def upload_file(self, local_file, remote_folder='', storage_type='Aspose', storage_name=None):
        if not local_file:
            raise ValueError("local_file not specified.")

        filename = os.path.basename(local_file)
        str_uri = self.str_uri_file
        if remote_folder:
            str_uri = str_uri + remote_folder + '/'

        str_uri += filename
        str_uri = Utils.append_storage(str_uri, '', storage_type, storage_name)
        signed_uri = Utils.sign(str_uri)
        response = Utils.upload_file_binary(local_file, signed_uri).json()
        if response['Status'] == 'OK':
            return True
        else:
            return False

    def get_files(self, remote_folder='', storage_type='Aspose', storage_name=None):
        str_uri = self.str_uri_folder + remote_folder
        str_uri = str_uri[:-1] if str_uri[-1] == '/' else str_uri
        str_uri = Utils.append_storage(str_uri, '', storage_type, storage_name)

        signed_uri = Utils.sign(str_uri)
        response = requests.get(signed_uri, headers={
            'content-type': 'application/json', 'accept': 'application/json'
        }).json()
        return response['Files']

    def get_file(self, filename, storage_type='Aspose', storage_name=None):
        if not filename:
            raise ValueError("filename not specified.")

        str_uri = self.str_uri_file + filename
        str_uri = Utils.append_storage(str_uri, '', storage_type, storage_name)

        signed_uri = Utils.sign(str_uri)
        response = requests.get(signed_uri, headers={
            'content-type': 'application/json', 'accept': 'application/json'
        }, stream=True)
        return response

    def file_exists(self, filename, storage_type='Aspose', storage_name=None):
        if not filename:
            raise ValueError("filename not specified.")

        str_uri = self.str_uri_exist + filename
        str_uri = Utils.append_storage(str_uri, '', storage_type, storage_name)

        signed_uri = Utils.sign(str_uri)
        response = requests.get(signed_uri, headers={
            'content-type': 'application/json', 'accept': 'application/json'
        }).json()
        return response['FileExist']['IsExist']

    def delete_file(self, filename, storage_type='Aspose', storage_name=None):
        if not filename:
            raise ValueError("filename not specified.")

        str_uri = self.str_uri_file + filename
        str_uri = Utils.append_storage(str_uri, '', storage_type, storage_name)

        signed_uri = Utils.sign(str_uri)
        response = requests.delete(signed_uri, headers={
            'content-type': 'application/json', 'accept': 'application/json'
        }).json()
        return True if response['Code'] == 200 else False

    def create_folder(self, folder_name, storage_type='Aspose', storage_name=None):
        if not folder_name:
            raise ValueError("folder_name not specified.")

        str_uri = self.str_uri_folder + folder_name
        str_uri = Utils.append_storage(str_uri, '', storage_type, storage_name)

        signed_uri = Utils.sign(str_uri)
        response = requests.put(signed_uri, '', headers={
            'content-type': 'application/json', 'accept': 'application/json'
        }).json()
        return True if response['Code'] == 200 else False

    def delete_folder(self, folder_name, storage_type='Aspose', storage_name=None):
        if not folder_name:
            raise ValueError("folder_name not specified.")

        str_uri = self.str_uri_folder + folder_name
        str_uri = Utils.append_storage(str_uri, '', storage_type, storage_name)

        signed_uri = Utils.sign(str_uri)
        response = requests.delete(signed_uri, headers={
            'content-type': 'application/json', 'accept': 'application/json'
        }).json()
        return True if response['Code'] == 200 else False

    def get_disc_usage(self, storage_type='Aspose', storage_name=None):
        str_uri = Utils.append_storage(self.str_uri_disc, '', storage_type, storage_name)

        signed_uri = Utils.sign(str_uri)
        response = requests.get(signed_uri, headers={
            'content-type': 'application/json', 'accept': 'application/json'
        }).json()
        return response['DiscUsage']
