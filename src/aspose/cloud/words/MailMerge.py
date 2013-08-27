
from aspose.cloud.common.asposeapp import AsposeApp
from aspose.cloud.common.product import Product
from aspose.cloud.common.utils import Utils
from aspose.cloud.storage.folder import Folder
import json

class WordMailMerge(object):
    
    def execute_mail_merge(self, file_name, str_xml):
        try:
            if file_name == "":
                raise Exception("Please Specify File Name")
            if str_xml == "":
                raise Exception("Please Specify Xml String")
            str_uri = Product.base_product_uri + "/words/" + file_name + "/executeMailMerge"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "POST", "", str_xml)
            json_data = json.loads(response_stream)
            v_output = Utils.validate_output(Utils(), response_stream)
            if v_output == "":
                folder = Folder()
                output_stream = folder.get_file(json_data["Document"]["FileName"])
                output_path = AsposeApp.output_location + file_name
                Utils.save_file(Utils(), output_stream, output_path)
                return output_path
            else:
                return v_output
        except:
            raise

    def execute_mailmerge_with_regions(self, file_name, str_xml):
        try:
            if file_name == "":
                raise Exception("Please Specify File Name")
            if str_xml == "":
                raise Exception("Please Specify Xml String")
            str_uri = Product.base_product_uri + "/words/" + file_name + "/executeMailMerge?withRegions=true"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "POST", "", str_xml)
            json_data = json.loads(response_stream)
            v_output = Utils.validate_output(Utils(), response_stream)
            if v_output == "":
                folder = Folder()
                output_stream = folder.get_file(json_data["Document"]["FileName"])
                output_path = AsposeApp.output_location + file_name
                Utils.save_file(Utils(), output_stream, output_path)
                return output_path
            else:
                return v_output
        except:
            raise
        
    def exectue_template(self, file_name, str_xml):
        try:
            if file_name == "":
                raise Exception("Please Specify File Name")
            if str_xml == "":
                raise Exception("Please Specify Xml String")
            str_uri = Product.base_product_uri + "/words/" + file_name + "/executeTemplate"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "POST", "", str_xml)
            json_data = json.loads(response_stream)
            v_output = Utils.validate_output(Utils(), response_stream)
            if v_output == "":
                folder = Folder()
                output_stream = folder.get_file(json_data["Document"]["FileName"])
                output_path = AsposeApp.output_location + file_name
                Utils.save_file(Utils(), output_stream, output_path)
                return output_path
            else:
                return v_output
        except:
            raise
