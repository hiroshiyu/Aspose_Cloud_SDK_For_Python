
from aspose.cloud.common.product import Product
from aspose.cloud.common.utils import Utils
import json
from aspose.cloud.storage.folder import Folder
from aspose.cloud.common.asposeapp import AsposeApp

class CellsTextEidtor(object):
    file_name = ""
    def __init__(self, file_name):
        self.file_name = file_name
        
    def find_text(self, *args):
        num_of_args = len(args)
        if num_of_args == 1:
            text = args[0]
        elif num_of_args == 2:
            worksheet_name = args[0]
            text = args[1]
        else:
            raise Exception("Wrong Numbers of Arguments")
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name
            if num_of_args == 2:
                str_uri += "/worksheet/" + worksheet_name
            str_uri += "/findText?text=" + text
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "POST", "", "")
            json_data = json.loads(response_stream)
            return json_data["TextItems"]["TextItemList"]
        except:
            raise
        
    def get_text_items(self, *args):
        num_of_args = len(args)
        if num_of_args == 1:
            worksheet_name = args[0]

        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name
            if num_of_args == 2:
                str_uri += "/worksheet/" + worksheet_name
            str_uri += "/textItems"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["TextItems"]["TextItemList"]
        except:
            raise
        
    def replace_text(self, *args):
        num_of_args = len(args)
        if num_of_args == 2:
            old_text = args[0]
            new_text = args[1]
        elif num_of_args == 3:
            worksheet_name = args[0]
            old_text = args[1]
            new_text = args[2]
        else:
            raise Exception("Wrong Numbers of Arguments")
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name
            if num_of_args == 3:
                str_uri += "/worksheet/" + worksheet_name
            str_uri += "/replaceText?oldValue=" + old_text + "&newValue=" + new_text
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "POST", "", "")
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
        
