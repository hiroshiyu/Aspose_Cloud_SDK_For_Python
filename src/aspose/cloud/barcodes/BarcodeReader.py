
from aspose.cloud.common.product import Product
from aspose.cloud.common.utils import Utils
import json
from aspose.cloud.storage.folder import Folder
from aspose.cloud.ntpath import basename
import sys
class BarcodeReader(object):
    filename = ""
    def __init__(self, filename):
        self.filename = filename
    def Read(self, symbology):
        try:
            if(self.filename == ""):
                raise Exception("Please Specify File Name")
            strURI = Product.base_product_uri + "/barcode/" + self.filename + "/recognize?" 
            if(symbology == ""):
                strURI += "type="
            else:
                strURI += "type=" + str(symbology)
            signedURI = Utils.sign(Utils(), strURI)
            response_stream = Utils.process_command(Utils(), signedURI, "GET", "JSON", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return json_data["Barcodes"]
            else:
                return False
        except:
            print sys.exc_info()[0]
            raise
        
    def ReadR(self, remote_image_name, remote_folder_name, barcode_read_type):
        try:
            if self.filename == "":
                raise Exception("Please Specify File Name")
            strURI = self.URIBuilder(remote_image_name, remote_folder_name, barcode_read_type)
            signedURI = Utils.sign(Utils(), strURI)
            response_stream = Utils.process_command(Utils(), signedURI, "GET", "JSON", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return json_data["Barcodes"]
            else:
                return False
        except:
            raise
    def ReadFromLocalFile(self, local_file_name, remote_folder_name, read_type):
        try:
            if self.filename == "":
                raise Exception("Please Specify File Name")
            folder = Folder()
            folder.upload_file(local_file_name, remote_folder_name)
            data = self.ReadR(basename(local_file_name), remote_folder_name, read_type)
            return data
        except:
            raise
        
    def URIBuilder(self, remote_image, remote_folder, read_type):
        uri = Product.base_product_uri + "/barcode/"
        if(remote_image != ""):
            uri += remote_image + "/"
        uri += "recognize?"
        if(read_type == "AllSupportedTypes"):
            uri += "type="
        else:
            uri += "type=" + str(read_type)
        if(remote_folder != ""):
            uri += "&folder=" + remote_folder
        return uri
