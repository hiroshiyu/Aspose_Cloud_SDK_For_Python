
from aspose.cloud.common.product import Product
from aspose.cloud.common.utils import Utils
import json
from aspose.cloud.storage.folder import Folder
from aspose.cloud.common.asposeapp import AsposeApp

class WordDocument(object):

    file_name = ""
    def __init__(self, file_name):
        self.file_name = file_name
        
    def append_document(self, append_docs=[], import_format_modes=[], source_folder=""):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if len(append_docs) != len(import_format_modes):
                raise Exception("Please specify complete documents and import format modes")
            str_uri = Product.base_product_uri + "/words/" + self.file_name + "/appendDocument"
            signed_uri = Utils.sign(Utils(), str_uri)
            data = {"DocumentEntries" : append_docs}
            json_data = json.dumps(data)
            response_stream = Utils.process_command(Utils(), signed_uri, "POST", "json", json_data)
            v_output = Utils.validate_output(Utils(), response_stream)
            if v_output == "":
                folder = Folder()
                uri = ""
                if source_folder is not "":
                    uri = "/" 
                output_stream = folder.get_file(uri + self.file_name)
                output_path = AsposeApp.output_location + self.file_name
                Utils.save_file(Utils(), output_stream, output_path)
                return output_path
            else:
                return v_output
        except:
            raise

    def get_document_info(self):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/words/" + self.file_name
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return json_data["Document"]
            else:
                return False
        except:
            raise

    def get_property(self, property_name):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if property_name == "":
                raise Exception("Please Specify Property Name")
            str_uri = Product.base_product_uri + "/words/" + self.file_name + "/documentProperties/" + property_name
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return json_data["DocumentProperty"]
            else:
                return False
        except:
            raise
            

    def set_property(self, property_name, property_value):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if property_name == "":
                raise Exception("Please Specify Property Name")
            if property_value == "":
                raise Exception("Please Specify Property Value")
            str_uri = Product.base_product_uri + "/words/" + self.file_name + "/documentProperties/" + property_name
            put_data = {"Value" : property_value}
            json_put = json.dumps(put_data)
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "PUT", "json", json_put)
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return json_data["DocumentProperty"]
            else:
                return False
        except:
            raise

    def delete_property(self, property_name):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if property_name == "":
                raise Exception("Please Specify Property Name")
            str_uri = Product.base_product_uri + "/words/" + self.file_name + "/documentProperties/" + property_name
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "DELETE", "", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return True
            else:
                return False
        except:
            raise

    def get_properties(self):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/words/" + self.file_name + "/documentProperties"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return json_data["DocumentProperties"]["List"]
            else:
                return False
        except:
            raise

    def convert_local_file(self, input_filename, output_filename, output_format):
        try:
            if input_filename == "":
                raise Exception("Please Specify Local File Name")
            if output_filename == "":
                raise Exception("Please Specify Output File Name")
            if output_format == "":
                raise Exception("Please Specify Output Format")
            str_uri = Product.base_product_uri + "/words/convert?format=" + output_format
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.upload_file_binary(Utils(), signed_uri, input_filename, "xml")
            v_output = Utils.validate_output(Utils(), response_stream)
            if v_output == "":
                if output_format == "html":
                    save_format = "zip"
                else:
                    save_format = output_format
                if output_filename == "":
                    output_path = AsposeApp.output_location + Utils.get_filename(Utils(), input_filename) + "." + save_format
                else:
                    output_path = AsposeApp.output_location + output_filename + "." + save_format
                Utils.save_file(Utils(), response_stream, output_path)
                return output_path
            else:
                return v_output
        except:
            raise
            
        
