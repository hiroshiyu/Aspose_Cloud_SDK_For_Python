__author__ = 'AssadMahmood'
import requests
import json

from asposecloud import AsposeApp
from asposecloud import Product
from asposecloud.common import Utils


class Document:

    def __init__(self, filename):
        self.filename = filename

        if not filename:
            raise ValueError("filename not specified")

        self.base_uri = Product.product_uri + 'pdf/' + self.filename

    def get_page_count(self, remote_folder='', storage_type='Aspose', storage_name=None):
        str_uri = self.base_uri + '/pages'
        str_uri = Utils.append_storage(str_uri, remote_folder, storage_type, storage_name)

        signed_uri = Utils.sign(str_uri)
        response = None
        try:
            response = requests.get(signed_uri, headers={
                'content-type': 'application/json', 'accept': 'application/json'
            })
            response.raise_for_status()
            response = response.json()
        except requests.HTTPError as e:
            print e
            print response.content
            exit(1)

        return len(response['Pages']['List']) if response['Pages']['List'] else 0

    def append_documents(self, append_file, start_page=None, end_page=None,
                         remote_folder='', storage_type='Aspose', storage_name=None):
        str_uri = self.base_uri + '/appendDocument'
        qry = {'appendFile': append_file}
        if start_page:
            qry['startPage'] = start_page
        if end_page:
            qry['endPage'] = end_page
        str_uri = Utils.build_uri(str_uri, qry)
        str_uri = Utils.append_storage(str_uri, remote_folder, storage_type, storage_name)

        signed_uri = Utils.sign(str_uri)
        response = None
        try:
            response = requests.post(signed_uri, None, headers={
                'content-type': 'application/json', 'accept': 'application/json'
            })
            response.raise_for_status()
            response = response.json()
        except requests.HTTPError as e:
            print e
            print response.content
            exit(1)

        validate_output = Utils.validate_result(response)
        if validate_output:
            return validate_output
        else:
            return True

    @staticmethod
    def merge_documents(merged_filename, source_files, remote_folder='', storage_type='Aspose', storage_name=None):

        json_data = json.dumps({'List': source_files})

        str_uri = Product.product_uri + 'pdf/' + merged_filename + '/merge'
        str_uri = Utils.append_storage(str_uri, remote_folder, storage_type, storage_name)

        signed_uri = Utils.sign(str_uri)
        response = None
        try:
            response = requests.put(signed_uri, json_data, headers={
                'content-type': 'application/json', 'accept': 'application/json'
            })
            response.raise_for_status()
            response = response.json()
        except requests.HTTPError as e:
            print e
            print response.content
            exit(1)

        return True if response['Status'] == 'OK' else False


class TextEditor:

    def __init__(self, filename):
        self.filename = filename

        if not filename:
            raise ValueError("filename not specified")

        self.base_uri = Product.product_uri + 'pdf/' + self.filename

    def get_fragment_count(self, page_number, remote_folder='', storage_type='Aspose', storage_name=None):
        str_uri = self.base_uri + '/pages/' + str(page_number) + '/fragments'
        str_uri = Utils.append_storage(str_uri, remote_folder, storage_type, storage_name)

        signed_uri = Utils.sign(str_uri)
        response = None
        try:
            response = requests.get(signed_uri, headers={
                'content-type': 'application/json', 'accept': 'application/json'
            })
            response.raise_for_status()
            response = response.json()
        except requests.HTTPError as e:
            print e
            print response.content
            exit(1)

        return len(response['TextItems']['List']) if response['TextItems']['List'] else 0

    def get_text(self, page_number, remote_folder='', storage_type='Aspose', storage_name=None):
        str_uri = self.base_uri + '/pages/' + str(page_number) + '/textitems'
        str_uri = Utils.append_storage(str_uri, remote_folder, storage_type, storage_name)

        signed_uri = Utils.sign(str_uri)
        response = None
        try:
            response = requests.get(signed_uri, headers={
                'content-type': 'application/json', 'accept': 'application/json'
            })
            response.raise_for_status()
            response = response.json()
        except requests.HTTPError as e:
            print e
            print response.content
            exit(1)

        output_text = ''
        for item in response['TextItems']['List']:
            output_text += item['Text']
        return output_text

    def get_text_items(self, page_number, remote_folder='', storage_type='Aspose', storage_name=None):
        str_uri = self.base_uri + '/pages/' + str(page_number) + '/textitems'
        str_uri = Utils.append_storage(str_uri, remote_folder, storage_type, storage_name)

        signed_uri = Utils.sign(str_uri)
        response = None
        try:
            response = requests.get(signed_uri, headers={
                'content-type': 'application/json', 'accept': 'application/json'
            })
            response.raise_for_status()
            response = response.json()
        except requests.HTTPError as e:
            print e
            print response.content
            exit(1)

        return response['TextItems']['List'] if response['TextItems']['List'] else False

    def replace_text(self, page_number, old_text, new_text, is_reg=False,
                     remote_folder='', storage_type='Aspose', storage_name=None):
        str_uri = self.base_uri + '/pages/' + str(page_number) + '/replaceText'
        str_uri = Utils.append_storage(str_uri, remote_folder, storage_type, storage_name)

        json_data = json.dumps({'OldValue': old_text, 'NewValue': new_text, 'Regex': is_reg})

        signed_uri = Utils.sign(str_uri)
        response = None
        try:
            response = requests.post(signed_uri, json_data, headers={
                'content-type': 'application/json', 'accept': 'application/json'
            })
            response.raise_for_status()
            response = response.json()
        except requests.HTTPError as e:
            print e
            print response.content
            exit(1)

        validate_output = Utils.validate_result(response)
        if not validate_output:
            return True
        else:
            return validate_output


class Extractor:

    def __init__(self, filename):
        self.filename = filename

        if not filename:
            raise ValueError("filename not specified")

        self.base_uri = Product.product_uri + 'pdf/' + self.filename

    def get_image(self, page_number, image_index, save_format, width=None, height=None,
                  remote_folder='', storage_type='Aspose', storage_name=None):
        if not save_format:
            raise ValueError("save_format not specified")

        if not page_number:
            raise ValueError("page_number not specified")

        str_uri = self.base_uri + '/pages/' + str(page_number) + '/images/' + str(image_index)
        qry = {'format': save_format}
        if width and height:
            qry['width'] = width
            qry['height'] = height
        str_uri = Utils.build_uri(str_uri, qry)
        str_uri = Utils.append_storage(str_uri, remote_folder, storage_type, storage_name)

        signed_uri = Utils.sign(str_uri)
        response = None
        try:
            response = requests.get(signed_uri, headers={
                'content-type': 'application/json', 'accept': 'application/json'
            }, stream=True)
            response.raise_for_status()
        except requests.HTTPError as e:
            print e
            print response.content
            exit(1)

        validate_output = Utils.validate_result(response)
        if not validate_output:
            output_path = AsposeApp.output_path + Utils.get_filename(self.filename) + '_' + str(page_number) \
                + '_' + str(image_index) + '.' + save_format
            Utils.save_file(response, output_path)
            return output_path
        else:
            return validate_output

    def get_image_count(self, page_number, remote_folder='', storage_type='Aspose', storage_name=None):
        if not page_number:
            raise ValueError("page_number not specified")

        str_uri = self.base_uri + '/pages/' + str(page_number) + '/images'
        str_uri = Utils.append_storage(str_uri, remote_folder, storage_type, storage_name)

        signed_uri = Utils.sign(str_uri)
        response = None
        try:
            response = requests.get(signed_uri, headers={
                'content-type': 'application/json', 'accept': 'application/json'
            })
            response.raise_for_status()
            response = response.json()
        except requests.HTTPError as e:
            print e
            print response.content
            exit(1)
        return len(response['Images']['List']) if response['Images']['List'] else 0


class Converter:

    def __init__(self, filename):
        self.filename = filename

        if not filename:
            raise ValueError("filename not specified")

        self.base_uri = Product.product_uri + 'pdf/' + self.filename

    def convert_to_image(self, page_number, save_format, remote_folder='', storage_type='Aspose', storage_name=None):
        if not save_format:
            raise ValueError("save_format not specified")

        if not page_number:
            raise ValueError("page_number not specified")

        str_uri = self.base_uri + '/pages/' + str(page_number)
        qry = {'format': save_format}
        str_uri = Utils.build_uri(str_uri, qry)
        str_uri = Utils.append_storage(str_uri, remote_folder, storage_type, storage_name)

        signed_uri = Utils.sign(str_uri)
        response = None
        try:
            response = requests.get(signed_uri, headers={
                'content-type': 'application/json', 'accept': 'application/json'
            }, stream=True)
            response.raise_for_status()
        except requests.HTTPError as e:
            print e
            print response.content
            exit(1)

        validate_output = Utils.validate_result(response)
        if not validate_output:
            output_path = AsposeApp.output_path + Utils.get_filename(self.filename) + '_' + str(page_number) + '.' + \
                save_format
            Utils.save_file(response, output_path)
            return output_path
        else:
            return validate_output

    def convert(self, save_format, remote_folder='', storage_type='Aspose', storage_name=None):
        if not save_format:
            raise ValueError("save_format not specified")

        str_uri = self.base_uri + '?format=' + save_format
        str_uri = Utils.append_storage(str_uri, remote_folder, storage_type, storage_name)

        signed_uri = Utils.sign(str_uri)
        response = None
        try:
            response = requests.get(signed_uri, headers={
                'content-type': 'application/json', 'accept': 'application/json'
            }, stream=True)
            response.raise_for_status()
        except requests.HTTPError as e:
            print e
            print response.content
            exit(1)

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
        response = None
        try:
            response = Utils.upload_file_binary(input_file, signed_uri)
            response.raise_for_status()
        except requests.HTTPError as e:
            print e
            print response.content
            exit(1)

        save_format = 'zip' if save_format == 'html' else save_format
        output_path = AsposeApp.output_path + Utils.get_filename(input_file) + '.' + save_format
        Utils.save_file(response, output_path)
        return output_path
