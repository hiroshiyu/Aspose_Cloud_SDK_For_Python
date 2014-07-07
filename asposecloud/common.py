__author__ = 'AssadMahmood'
import requests
import hmac
import hashlib
import re
import string
import os
import json

from urlparse import urlparse
from asposecloud import AsposeApp


class Utils:

    def __init__(self):
        return

    @staticmethod
    def build_uri(path, qry_data=None):
        qry_str = ''
        for key, value in qry_data.iteritems():
            qry_str += str(key) + '=' + str(value) + '&'

        if qry_str:
            uri = path + '?' + qry_str[:-1]
        else:
            uri = path
        return uri

    @staticmethod
    def validate_result(result):
        if type(result) == requests.Response:
            result = result.content
        elif type(result) == dict:
            result = json.dumps(result)

        results = ['Unknown file format', 'Unable to read beyond the end of the stream', 'Index was out of range',
                   'Cannot read that as a ZipFile', 'Not a Microsoft PowerPoint 2007 presentation',
                   'Index was outside the bounds of the array',
                   'An attempt was made to move the position before the beginning of the stream']
        for val in results:
            if re.search(val, result):
                return val

        return None

    @staticmethod
    def upload_file_binary(local_file, uri):
        with open(local_file, 'rb') as payload:
            return requests.put(uri, payload, stream=True)

    @staticmethod
    def sign(url_to_sign):
        url_to_sign = url_to_sign.replace(" ", "%20")
        url = urlparse(url_to_sign)

        if url.query == "":
            url_part_to_sign = url.scheme + "://" + url.netloc + url.path + "?appSID=" + AsposeApp.app_sid
        else:
            url_part_to_sign = url.scheme + "://" + url.netloc + url.path + "?" + url.query + "&appSID=" + \
                AsposeApp.app_sid

        signature = hmac.new(AsposeApp.app_key, url_part_to_sign, hashlib.sha1).digest().encode('base64')[:-1]
        signature = re.sub('[=_-]', '', signature)

        if url.query == "":
            return url.scheme + "://" + url.netloc + url.path + "?appSID=" + AsposeApp.app_sid + "&signature=" + \
                signature
        else:
            return url.scheme + "://" + url.netloc + url.path + "?" + url.query + "&appSID=" + AsposeApp.app_sid + \
                "&signature=" + signature

    @staticmethod
    def append_storage(uri, remote_folder='', storage_type='Aspose', storage_name=''):

        tmp_uri = None

        if remote_folder and not remote_folder.isspace():
            tmp_uri = "folder=" + remote_folder + "&"

        if storage_name and not storage_type == "Aspose":
            tmp_uri = tmp_uri + "storage=" + storage_name

        if tmp_uri:
            if string.find(tmp_uri, '?'):
                tmp_uri = "&" + tmp_uri
            else:
                tmp_uri = "?" + tmp_uri

        if tmp_uri:
            if tmp_uri[-1:] == '&':
                tmp_uri = tmp_uri[:-1]

        if tmp_uri:
            return uri + tmp_uri
        else:
            return uri

    @staticmethod
    def save_file(response_stream, filename):
        with open(filename, 'wb') as f:
            for chunk in response_stream.iter_content():
                f.write(chunk)

    @staticmethod
    def get_filename(filename):
        return os.path.splitext(os.path.basename(filename))[0]