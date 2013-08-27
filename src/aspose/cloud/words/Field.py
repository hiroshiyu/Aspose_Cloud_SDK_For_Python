
import json
from aspose.cloud.common.product import Product
from aspose.cloud.common.utils import Utils
from aspose.cloud.storage.folder import Folder
from aspose.cloud.common.asposeapp import AsposeApp

class WordField(object):
    
    def insert_page_number(self, file_name, alignment, text_format, is_top, set_page_number_on_first_page):
        try:
            if file_name == "":
                raise Exception("Please Specify File Name")
            field_arr = {"Format" : text_format , "Alignment" : alignment, "IsTop" : str(is_top), "SetPageNumberOnFirstPage" : str(set_page_number_on_first_page)}
            json_data = json.dumps(field_arr)
            str_uri = Product.base_product_uri + "/words/" + file_name + "/insertPageNumber"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "POST", "json", json_data)
            v_output = Utils.validate_output(Utils(), response_stream)
            if v_output == "":
                folder = Folder()
                output_stream = folder.get_file(file_name)
                output_path = AsposeApp.output_location + file_name
                Utils.save_file(Utils(), output_stream, output_path)
                return output_path
            else:
                return v_output
        except:
            raise

    def get_mailmerge_field_names(self, file_name):
        try:
            if file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/words/" + file_name + "/mailMergeFieldNames"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET" , "", "")
            json_data = json.loads(response_stream)
            return json_data["FieldNames"]
        except:
            raise
            
