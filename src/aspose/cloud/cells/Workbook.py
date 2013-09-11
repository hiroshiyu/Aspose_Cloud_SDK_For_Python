
from aspose.cloud.common.product import Product
from aspose.cloud.common.utils import Utils
import json

class Workbook(object):
    file_name = ""
    def __init__(self, file_name):
        self.file_name = file_name
        
    def get_properties(self):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/documentProperties"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return json_data["DocumentProperties"]["DocumentPropertyList"]
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
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/documentProperties/" + property_name
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
            put_data = {"Value" : property_value}
            json_arr = json.dumps(put_data)
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/documentProperties/" + property_name
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "PUT", "json", json_arr)
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return json_data["DocumentProperty"]
            else:
                return False
        except:
            raise

    def remove_all_properties(self):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/documentProperties"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "DELETE", "", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return True
            else:
                return False
        except:
            raise

    def remove_property(self, property_name):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if property_name == "":
                raise Exception("Please Specify Property Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/documentProperties/" + property_name
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "DELETE", "", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return True
            else:
                return False
        except:
            raise

    def create_empty_workbook(self):
        try:
            str_uri = Product.base_product_uri + "/cells/" + self.file_name
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "PUT", "", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return json_data
            else:
                return False
        except:
            raise
        
    def create_workbook_from_template(self, template_filename):
        try:
            if template_filename == "":
                raise Exception("Please Specify Template File Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "?templatefile=" + template_filename
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "PUT", "", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return json_data
            else:
                return False
        except:
            raise
        
    def create_workbook_from_smartmarker_template(self, template_filename, data_file):
        try:
            if template_filename == "":
                raise Exception("Please Specify Template File Name")
            if data_file == "":
                raise Exception("Please Specify Template Data File")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "?templatefile=" + template_filename + "&dataFile=" + data_file
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "PUT", "", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return json_data
            else:
                return False
        except:
            raise

    def process_smartmarker(self, data_file):
        try:
            if data_file == "":
                raise Exception("Please Specify Template Data File")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/smartmarker?xmlFile=" + data_file
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "POST", "", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return json_data
            else:
                return False
        except:
            raise

    def get_worksheets_count(self):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return len(json_data["Worksheets"]["WorksheetList"])
            else:
                return False
        except:
            raise
        
    def get_names_count(self):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/names"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return len(json_data["Names"])
            else:
                return False
        except:
            raise

    def get_default_style(self):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/defaultStyle"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return json_data["Style"]
            else:
                return False
        except:
            raise
        
    def encrypt_workbook(self, encryption_type , password, key_length):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            post_data = {"EncriptionType" : encryption_type , "Password" : password, "KeyLength" : str(key_length)}
            json_arr = json.dumps(post_data)
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/encryption"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "POST", "json", json_arr)
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return True
            else:
                return False
        except:
            raise

    def protect_workbook(self, protection_type , password):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            post_data = {"ProtectionType" : protection_type , "Password" : password}
            json_arr = json.dumps(post_data)
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/protection"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "POST", "json", json_arr)
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return True
            else:
                return False
        except:
            raise
        
    def unprotect_workbook(self, password):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            post_data = {"Password" : password}
            json_arr = json.dumps(post_data)
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/protection"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "DELETE", "json", json_arr)
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return True
            else:
                return False
        except:
            raise
        
    def set_modify_password(self, password):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            post_data = {"Password" : password}
            json_arr = json.dumps(post_data)
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/writeProtection"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "PUT", "json", json_arr)
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return True
            else:
                return False
        except:
            raise
        
    def clear_modify_password(self, password):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            post_data = {"Password" : password}
            json_arr = json.dumps(post_data)
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/writeProtection"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "DELETE", "json", json_arr)
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return True
            else:
                return False
        except:
            raise
        
    def decrypt_workbook(self, password):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            post_data = {"Password" : password }
            json_arr = json.dumps(post_data)
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/encryption"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "DELETE", "json", json_arr)
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return True
            else:
                return False
        except:
            raise

    def add_worksheet(self, worksheet_name):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if worksheet_name == "":
                raise Exception("Please Specify Worksheet Name")            
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + worksheet_name
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "PUT", "", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 201:
                return True
            else:
                return False
        except:
            raise
        
    def delete_worksheet(self, worksheet_name):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if worksheet_name == "":
                raise Exception("Please Specify Worksheet Name")            
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + worksheet_name
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "DELETE", "", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return True
            else:
                return False
        except:
            raise
        
    def merge_workbook(self, merge_filename):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if merge_filename == "":
                raise Exception("Please Specify Merge File Name")            
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/merge?mergeWith=" + merge_filename
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "POST", "", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return True
            else:
                return False
        except:
            raise
