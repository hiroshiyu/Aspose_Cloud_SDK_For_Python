
from aspose.cloud.common.product import Product
from aspose.cloud.common.utils import Utils
import json
from aspose.cloud.storage.folder import Folder
from aspose.cloud.common.asposeapp import AsposeApp



class SlideDocument(object):
    file_name = ""
    def __init__(self, file_name):
        self.file_name = file_name
    def get_slides_count(self, stroage_type=None, storage_name=None, folder=None):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/slides/" + self.file_name + "/slides"
            if folder is not None:
                str_uri += "?folder=" + folder
            if storage_name is not None:
                str_uri += "&storage=" + storage_name
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "JSON", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return len(json_data["Slides"]["SlideList"])
            else:
                return False
        except:
            raise
        
    def replace_text(self, *args):
        num_of_args = len(args)
        if(num_of_args == 2):
            old_text = args[0]
            new_text = args[1]
        elif(num_of_args == 3):
            old_text = args[0]
            new_text = args[1]
            slide_number = args[2]
        else:
            raise Exception("Invalid Numbers of Arguments")
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/slides/" + self.file_name
            if num_of_args == 3:
                str_uri += "/slides/" + str(slide_number)
            str_uri += "/replaceText?oldValue=" + old_text + "&newValue=" + new_text + "&ignoreCase=true"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "POST", "JSON", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return str(json_data["Matches"]) + " Found And Replaced"
            else:
                return False
        except:
            raise

    def get_all_text_items(self, *args):
        num_of_args = len(args)
        if num_of_args > 0:
            slide_number = args[0]
            with_empty = args[1]
        
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/slides/" + self.file_name
            if num_of_args == 2:
                str_uri += "/slides/" + str(slide_number) + "/textItems?withEmpty=" + str(with_empty)
            else:
                str_uri += "/textItems"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = signed_uri = Utils.process_command(Utils(), signed_uri, "GET", "JSON", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return json_data["TextItems"]["Items"]
            else:
                return False
            
        except:
            raise
    
    def delete_all_slides(self,storage_type = None,storage_name = None, folder= None):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/slides/" + self.file_name + "/slides"
            if folder is not None:
                str_uri += "?folder=" + folder
            if storage_name is not None:
                str_uri += "&storage=" + storage_name
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "DELETE", "JSON", "")
            v_output = Utils.validate_output(Utils(), response_stream)
            if(v_output == ""):
                folder = Folder()
                response_stream = folder.get_file(self.file_name)
                output_path = AsposeApp.output_location + self.file_name
                Utils.save_file(Utils(), response_stream, output_path)
                return output_path
            else:
                return v_output
        except:
            raise
    
    def get_document_properties(self):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/slides/" + self.file_name + "/documentProperties"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "JSON", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return json_data["DocumentProperties"]["List"]
            else:
                return False
        except:
            raise
    def get_document_property(self, property_name):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if property_name == "":
                raise Exception("Please Specify Property Name")
            str_uri = Product.base_product_uri + "/slides/" + self.file_name + "/presentation/documentProperties/" + property_name
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "JSON", "")
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
            str_uri = Product.base_product_uri + "/slides/" + self.file_name + "/documentProperties"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "DELETE", "JSON", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return True
            else:
                return False
        except:
            raise
    def delete_document_property(self, property_name):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/slides/" + self.file_name + "/documentProperties/" + property_name
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "DELETE", "", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return True
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
                put_data_arr = {'Value' : property_value}
                put_data = json.dumps(put_data_arr)
                str_uri = Product.base_product_uri + "/slides/" + self.file_name + "/documentProperties/" + property_name
                signed_uri = Utils.sign(Utils(), str_uri)
                response_stream = Utils.process_command(Utils(), signed_uri, "PUT", "JSON", put_data)
                json_data = json.loads(response_stream)
                if json_data["Code"] == 200:
                    return True
                else:
                    return False
            except:
                raise
    def add_custom_property(self, properties_list):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if properties_list == "":
                raise Exception("Please Specify File Name")
            put_data = json.dumps(properties_list)
            str_uri = Product.base_product_uri + "/slides/" + self.file_name + "/documentProperties"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "PUT", "JSON", put_data)
            return response_stream
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return json_data
            else:
                return False
        except:
            raise
        
    def save_as(self, output_path, save_format,storage_type = None,storage_name = None,folder=None):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if output_path == "":
                raise Exception("Please Specify Output Path")
            if save_format == "":
                raise Exception("Please Specify Save Format")
            str_uri = Product.base_product_uri + "/slides/" + self.file_name + "?format=" + save_format
            if folder is not None:
                str_uri += "?folder=" + folder
            if storage_name is not None:
                str_uri += "&storage=" + storage_name
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            v_output = Utils.validate_output(Utils(), response_stream)
            if(v_output == ""):
                Utils.save_file(Utils(), response_stream, output_path + Utils.get_filename(Utils(), self.file_name) + "." + save_format)
                return True
            else:
                return v_output
        except:
            raise
    def save_slide_as(self, slide_number, output_path, save_format):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if output_path == "":
                raise Exception("Please Specify Output Path")
            if save_format == "":
                raise Exception("Please Specify Save Format")
            if slide_number == "" or slide_number == 0:
                raise Exception("Please Specify Slide Number")
            str_uri = Product.base_product_uri + "/slides/" + self.file_name + "/slides/" + str(slide_number) + "?format=" + save_format
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            v_output = Utils.validate_output(Utils(), response_stream)
            if(v_output == ""):
                Utils.save_file(Utils(), response_stream, output_path + Utils.get_filename(Utils(), self.file_name) + "." + save_format)
                return True
            else:
                return v_output
        except:
            raise
