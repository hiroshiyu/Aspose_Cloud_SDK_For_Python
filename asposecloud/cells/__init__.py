__author__ = 'AssadMahmood'
import requests

from asposecloud import AsposeApp
from asposecloud import Product
from asposecloud.common import Utils

# ========================================================================
# EXTRACTOR CLASS
# ========================================================================


class Extractor:

    def __init__(self, filename):
        self.filename = filename

        if not filename:
            raise ValueError("filename not specified")

        self.base_uri = Product.product_uri + 'cells/' + self.filename

    def get_autoshape(self, shape_index, worksheet_name, save_format, password=None,
                           remote_folder='', storage_type='Aspose', storage_name=None):
        str_uri = self.base_uri + '/worksheets/' + worksheet_name + '/autoshapes/' + str(shape_index)
        qry = {'format': save_format}
        if not password is None:
            qry['password'] = password
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
            save_format = 'zip' if save_format == 'html' else save_format
            output_path = AsposeApp.output_path + Utils.get_filename(self.filename) + '_shape_' + str(shape_index)\
                + '.' + save_format
            Utils.save_file(response, output_path)
            return output_path
        else:
            return validate_output

    def get_chart(self, chart_index, worksheet_name, save_format, password=None,
                       remote_folder='', storage_type='Aspose', storage_name=None):
        str_uri = self.base_uri + '/worksheets/' + worksheet_name + '/charts/' + str(chart_index)
        qry = {'format': save_format}
        if not password is None:
            qry['password'] = password
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
            save_format = 'zip' if save_format == 'html' else save_format
            output_path = AsposeApp.output_path + Utils.get_filename(self.filename) + '_chart_' + str(chart_index)\
                + '.' + save_format
            Utils.save_file(response, output_path)
            return output_path
        else:
            return validate_output

    def get_oleobject(self, ole_index, worksheet_name, save_format, password=None,
                           remote_folder='', storage_type='Aspose', storage_name=None):
        str_uri = self.base_uri + '/worksheets/' + worksheet_name + '/oleobjects/' + str(ole_index)
        qry = {'format': save_format}
        if not password is None:
            qry['password'] = password
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
            save_format = 'zip' if save_format == 'html' else save_format
            output_path = AsposeApp.output_path + Utils.get_filename(self.filename) + '_ole_' + str(ole_index)\
                + '.' + save_format
            Utils.save_file(response, output_path)
            return output_path
        else:
            return validate_output

    def get_picture(self, picture_index, worksheet_name, save_format, password=None,
                         remote_folder='', storage_type='Aspose', storage_name=None):
        str_uri = self.base_uri + '/worksheets/' + worksheet_name + '/pictures/' + str(picture_index)
        qry = {'format': save_format}
        if not password is None:
            qry['password'] = password
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
            save_format = 'zip' if save_format == 'html' else save_format
            output_path = AsposeApp.output_path + Utils.get_filename(self.filename) + '_pic_' + str(picture_index)\
                + '.' + save_format
            Utils.save_file(response, output_path)
            return output_path
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

        self.base_uri = Product.product_uri + 'cells/' + self.filename

    def autoshape_to_image(self, shape_index, worksheet_name, save_format, password=None,
                           remote_folder='', storage_type='Aspose', storage_name=None):
        str_uri = self.base_uri + '/worksheets/' + worksheet_name + '/autoshapes/' + str(shape_index)
        qry = {'format': save_format}
        if not password is None:
            qry['password'] = password
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
            save_format = 'zip' if save_format == 'html' else save_format
            output_path = AsposeApp.output_path + Utils.get_filename(self.filename) + '_shape_' + str(shape_index)\
                + '.' + save_format
            Utils.save_file(response, output_path)
            return output_path
        else:
            return validate_output

    def chart_to_image(self, chart_index, worksheet_name, save_format, password=None,
                       remote_folder='', storage_type='Aspose', storage_name=None):
        str_uri = self.base_uri + '/worksheets/' + worksheet_name + '/charts/' + str(chart_index)
        qry = {'format': save_format}
        if not password is None:
            qry['password'] = password
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
            save_format = 'zip' if save_format == 'html' else save_format
            output_path = AsposeApp.output_path + Utils.get_filename(self.filename) + '_chart_' + str(chart_index)\
                + '.' + save_format
            Utils.save_file(response, output_path)
            return output_path
        else:
            return validate_output

    def oleobject_to_image(self, ole_index, worksheet_name, save_format, password=None,
                           remote_folder='', storage_type='Aspose', storage_name=None):
        str_uri = self.base_uri + '/worksheets/' + worksheet_name + '/oleobjects/' + str(ole_index)
        qry = {'format': save_format}
        if not password is None:
            qry['password'] = password
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
            save_format = 'zip' if save_format == 'html' else save_format
            output_path = AsposeApp.output_path + Utils.get_filename(self.filename) + '_ole_' + str(ole_index)\
                + '.' + save_format
            Utils.save_file(response, output_path)
            return output_path
        else:
            return validate_output

    def picture_to_image(self, picture_index, worksheet_name, save_format, password=None,
                         remote_folder='', storage_type='Aspose', storage_name=None):
        str_uri = self.base_uri + '/worksheets/' + worksheet_name + '/pictures/' + str(picture_index)
        qry = {'format': save_format}
        if not password is None:
            qry['password'] = password
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
            save_format = 'zip' if save_format == 'html' else save_format
            output_path = AsposeApp.output_path + Utils.get_filename(self.filename) + '_pic_' + str(picture_index)\
                + '.' + save_format
            Utils.save_file(response, output_path)
            return output_path
        else:
            return validate_output

    def convert_to_image(self, worksheet_name, save_format, password=None,
                         remote_folder='', storage_type='Aspose', storage_name=None):
        if not save_format:
            raise ValueError("save_format not specified")

        str_uri = self.base_uri + '/worksheets/' + worksheet_name
        qry = {'format': save_format}
        if not password is None:
            qry['password'] = password
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
            save_format = 'zip' if save_format == 'html' else save_format
            output_path = AsposeApp.output_path + Utils.get_filename(self.filename) + '.' + save_format
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

        str_uri = Product.product_uri + 'cells/convert?format=' + save_format

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
