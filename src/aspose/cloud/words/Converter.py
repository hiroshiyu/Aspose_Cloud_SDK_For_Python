from aspose.cloud.common.product import Product
from aspose.cloud.common.utils import Utils
from aspose.cloud.common.asposeapp import AsposeApp

class WordConverter(object):
    file_name = ""
    save_format = ""
    def __init__(self, file_name):
        self.file_name = file_name
        self.save_format = "doc"
        
    def convert(self):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/words/" + self.file_name + "?format=" + self.save_format
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            v_output = Utils.validate_output(Utils(), response_stream)
            if(v_output == ""):
                output_path = AsposeApp.output_location + Utils.get_filename(Utils(), self.file_name) + "." + self.save_format
                Utils.save_file(Utils(), response_stream, output_path)
                return output_path
            else:
                return v_output
        except:
            raise
    def convert_local_file(self, input_path, output_path, output_format):
        try:
            if input_path == "":
                raise Exception("Please Specify Input File with path")
            if output_path == "":
                raise Exception("Please Specify Output File With Path")
            if output_format == "":
                raise Exception("Please Specify Output Format with path")
            str_uri = Product.base_product_uri + "/words/convert?format=" + output_format
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.upload_file_binary(Utils(), signed_uri, input_path, "xml")
            v_output = Utils.validate_output(Utils(), response_stream)
            if v_output == "":
                if output_format == "html":
                    save_format = "zip"
                else:
                    save_format = output_format
                output_file = AsposeApp.output_location + Utils.get_filename(Utils(), input_path) + "." + save_format
                Utils.save_file(Utils(), response_stream, output_file)
                return output_file
            else:
                return v_output
        except:
            raise  
