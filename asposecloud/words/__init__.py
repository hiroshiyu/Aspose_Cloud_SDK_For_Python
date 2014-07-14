__author__ = 'AssadMahmood'
import requests
import json

from asposecloud import AsposeApp
from asposecloud import Product
from asposecloud.common import Utils


# ========================================================================
# MAIL MERGE CLASS
# ========================================================================


class MailMerge:

    def __init__(self, filename):
        self.filename = filename

        if not filename:
            raise ValueError("filename not specified")

        self.base_uri = Product.product_uri + 'words/' + self.filename

    def execute(self, str_xml, with_regions=False, remote_folder='', storage_type='Aspose', storage_name=None):
        if not str_xml:
            raise ValueError("str_xml not specified")

        str_uri = self.base_uri + '/executeMailMerge'
        str_uri = str_uri + '?withRegions=true' if with_regions else str_uri
        str_uri = Utils.append_storage(str_uri, remote_folder, storage_type, storage_name)

        signed_uri = Utils.sign(str_uri)
        response = None
        try:
            response = requests.post(signed_uri, str_xml, headers={
                'content-type': 'application/xml', 'accept': 'application/json'
            })
            response.raise_for_status()
            response = response.json()
        except requests.HTTPError as e:
            print e
            print response.content
            exit(1)

        validate_output = Utils.validate_result(response)
        if not validate_output:
            return Utils.download_file(self.filename, self.filename, remote_folder, storage_type, storage_name)
        else:
            return validate_output

    def execute_template(self, str_xml, with_regions=False, remote_folder='', storage_type='Aspose', storage_name=None):
        if not str_xml:
            raise ValueError("str_xml not specified")

        str_uri = self.base_uri + '/executeTemplate'
        str_uri = str_uri + '?withRegions=true' if with_regions else str_uri
        str_uri = Utils.append_storage(str_uri, remote_folder, storage_type, storage_name)

        signed_uri = Utils.sign(str_uri)
        response = None
        try:
            response = requests.post(signed_uri, str_xml, headers={
                'content-type': 'application/xml', 'accept': 'application/json'
            })
            response.raise_for_status()
            response = response.json()
        except requests.HTTPError as e:
            print e
            print response.content
            exit(1)

        validate_output = Utils.validate_result(response)
        if not validate_output:
            return Utils.download_file(self.filename, self.filename, remote_folder, storage_type, storage_name)
        else:
            return validate_output

# ========================================================================
# BUILDER CLASS
# ========================================================================


class Builder:

    def __init__(self, filename):
        self.filename = filename

        if not filename:
            raise ValueError("filename not specified")

        self.base_uri = Product.product_uri + 'words/' + self.filename

    def insert_watermark_image(self, image_file, angle, remote_folder='', storage_type='Aspose', storage_name=None):
        str_uri = self.base_uri + '/insertWatermarkText'
        qry = {'imageFile': image_file, 'rotationAngle': angle}
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
        if not validate_output:
            return Utils.download_file(self.filename, self.filename, remote_folder, storage_type, storage_name)
        else:
            return validate_output

    def insert_watermark_text(self, text, angle, remote_folder='', storage_type='Aspose', storage_name=None):
        str_uri = self.base_uri + '/insertWatermarkText'
        str_uri = Utils.append_storage(str_uri, remote_folder, storage_type, storage_name)

        json_data = json.dumps({'Text': text, 'RotationAngle': angle})

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
            return Utils.download_file(self.filename, self.filename, remote_folder, storage_type, storage_name)
        else:
            return validate_output

    def replace_text(self, old_text, new_text, match_case=False, match_whole_word=False,
                     remote_folder='', storage_type='Aspose', storage_name=None):
        str_uri = self.base_uri + '/replaceText'
        str_uri = Utils.append_storage(str_uri, remote_folder, storage_type, storage_name)

        json_data = json.dumps({'OldValue': old_text, 'NewValue': new_text,
                                'IsMatchCase': match_case, 'IsMatchWholeWord': match_whole_word})

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

# ========================================================================
# CONVERTER CLASS
# ========================================================================


class Converter:

    def __init__(self, filename):
        self.filename = filename

        if not filename:
            raise ValueError("filename not specified")

        self.base_uri = Product.product_uri + 'words/' + self.filename

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

        validate_output = Utils.validate_result(response)
        if not validate_output:
            save_format = 'zip' if save_format == 'html' else save_format
            output_path = AsposeApp.output_path + Utils.get_filename(self.filename) + '.' + save_format
            Utils.save_file(response, output_path)
            return output_path
        else:
            return validate_output

    @staticmethod
    def convert_local_file(input_file, save_format):
        if not input_file:
            raise ValueError("input_file not specified")

        if not save_format:
            raise ValueError("save_format not specified")

        str_uri = Product.product_uri + 'words/convert?format=' + save_format

        signed_uri = Utils.sign(str_uri)
        response = None
        try:
            response = Utils.upload_file_binary(input_file, signed_uri)
            response.raise_for_status()
        except requests.HTTPError as e:
            print e
            print response.content
            exit(1)

        validate_output = Utils.validate_result(response)
        if not validate_output:
            save_format = 'zip' if save_format == 'html' else save_format
            output_path = AsposeApp.output_path + Utils.get_filename(input_file) + '.' + save_format
            Utils.save_file(response, output_path)
            return output_path
        else:
            return validate_output
