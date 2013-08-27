
from aspose.cloud.common.product import Product
from aspose.cloud.common.utils import Utils
import json
from aspose.cloud.storage.folder import Folder
from aspose.cloud.common.asposeapp import AsposeApp
class TextEditor:
    file_name = ""
    
    def __init__(self, file_name):
        self.file_name = file_name
    
    def get_text(self, *arg):
        try:
            if self.file_name == "":
                raise Exception("Please Specify Pdf File Name")
            if len(arg) > 0:
                page_number = arg[0]
            str_uri = Product.base_product_uri + "/pdf/" + self.file_name
            if len(arg) is not 0:
                str_uri += "/pages" + str(page_number) + "/TextItems"
            else:
                str_uri += "/TextItems"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            raw_text = ""
            for item in json_data["TextItems"]["List"]:
                item["Text"].encode('utf8')
                raw_text += item["Text"].encode('utf-8')
            return raw_text
        except:
            raise

    def get_text_items(self, *arg):
        try:
            if self.file_name == "":
                raise Exception("Please Specify Pdf File Name")
            if len(arg) == 1:
                page_number = arg[0]
            elif len(arg) == 2:
                page_number = arg[0]
                fragment_number = arg[1]
            str_uri = Product.base_product_uri + "/pdf/" + self.file_name
            if len(arg) == 1:
                str_uri += "/pages/" + str(page_number) + "/TextItems"
            elif len(arg) == 2:
                str_uri += "/pages/" + str(page_number) + "/fragments/" + str(fragment_number) + "/TextItems"
            else:
                str_uri += "/TextItems"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["TextItems"]["List"]                
        except:
            raise   

    def get_fragment_count(self, page_number):
        try:
            if self.file_name == "":
                raise Exception("Please Specify Pdf File Name")            
            str_uri = Product.base_product_uri + "/pdf/" + self.file_name + "/pages/" + str(page_number) + "/fragments"            
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return len(json_data["TextItems"]["List"])                
        except:
            raise   
    
    def get_segment_count(self, page_number, fragment_number):
        try:
            if self.file_name == "":
                raise Exception("Please Specify Pdf File Name")
            if page_number == "":
                raise Exception("Please Specify Page Number")
            if fragment_number == "":
                raise Exception("Please Specify Fragment Number")          
            str_uri = Product.base_product_uri + "/pdf/" + self.file_name + "/pages/" + str(page_number) + "/fragments/" + str(fragment_number)            
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return len(json_data["TextItems"]["List"])                
        except:
            raise
        
    def get_text_format(self, page_number, fragment_number, segment_number=None):
        try:
            if self.file_name == "":
                raise Exception("Please Specify Pdf File Name") 
            str_uri = Product.base_product_uri + "/pdf/" + self.file_name + "/pages/" + str(page_number) + "/fragments/" + str(fragment_number)
            if segment_number is not None:
                str_uri += "/segments/" + str(segment_number)
            str_uri += "/textformat"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["TextFormat"]
        except:
            raise

    def replace_text(self, old_text, new_text, is_regular_expression=False, page_number=0):
        try:
            if self.file_name == '':
                raise Exception('filename not specified')
            if old_text == '':
                raise Exception('old text not specified')
          
            if new_text == '':
                raise Exception('new text not specified')
            post_hash = { "OldValue" : old_text, "NewValue" : new_text, "Regex": "false" }
            json_data = json.dumps(post_hash)
            if page_number > 0:
                str_uri = Product.base_product_uri + "/pdf/" + self.file_name + "/pages/" + str(page_number) + '/replaceText'
            else:
                str_uri = Product.base_product_uri + "/pdf/" + self.file_name + '/replaceText'
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "POST", "json", json_data)
            v_output = Utils.validate_output(Utils(), response_stream)
            if v_output == "":
                folder = Folder()
                output_stream = folder.get_file(self.file_name)
                output_path = AsposeApp.output_location + self.file_name
                Utils.save_file(Utils(), output_stream, output_path)
                return output_path
            else:
                return v_output
        except:
            raise
