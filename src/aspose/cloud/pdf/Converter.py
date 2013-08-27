from aspose.cloud.common.asposeapp import AsposeApp
from aspose.cloud.common.product import Product
from aspose.cloud.common.utils import Utils
import os

class PdfConverter(object):
   
    file_name = ""
    save_format = ""

    def __init__(self, file_name):
        self.file_name = file_name
        self.save_format = "pdf"
        
    def convert_to_image_by_size(self, page_number, image_format, width, height):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/pdf/" + self.file_name + "/pages/" + str(page_number) + "?format=" + image_format + "&width=" + str(width) + "&height" + str(height)
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            v_output = Utils.validate_output(Utils(), response_stream)
            if v_output == "":
                output_path = AsposeApp.output_location + Utils.get_filename(Utils(), self.file_name) + "_" + str(page_number) + "." + image_format
                Utils.save_file(Utils(), response_stream, output_path)
                return output_path
            else:
                return v_output
        except:
            raise

    def convert_to_image(self, page_number, image_format):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/pdf/" + self.file_name + "/pages/" + str(page_number) + "?format=" + image_format
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            v_output = Utils.validate_output(Utils(), response_stream)
            if v_output == "":
                output_path = AsposeApp.output_location + Utils.get_filename(Utils(), self.file_name) + "_" + str(page_number) + "." + image_format
                Utils.save_file(Utils(), response_stream, output_path)
                return output_path
            else:
                return v_output
        except:
            raise

    def convert(self):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/pdf/" + self.file_name + "?format=" + self.save_format
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            v_output = Utils.validate_output(Utils(), response_stream)
            if v_output == "":
                if self.save_format == "html":
                    save_format = "zip"
                else:
                    save_format = self.save_format
                output_path = AsposeApp.output_location + Utils.get_filename(Utils(), self.file_name) + "." + save_format
                Utils.save_file(Utils(), response_stream, output_path)
                return output_path
            else:
                return v_output
        except:
            raise

    def convert_local_file(self, input_file, output_filename, output_format):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if input_file == "":
                raise Exception("Please Specify Input File Along With Path")
            if output_filename == "":
                raise Exception("Please Specify Output File Name")
            if output_format == "":
                raise Exception("Please Specify Output Format")
            str_uri = Product.base_product_uri + "/pdf/convert?format=" + output_format
            if os.path.exists(input_file) == False:
                raise Exception("Input File Does not Exists")
            signed_uri = Utils.sign(Utils(), str_uri)
            
            response_stream = Utils.upload_file_binary(Utils(), signed_uri, input_file)
            v_output = Utils.validate_output(Utils(), response_stream)
            if v_output == "":
                if self.save_format == "html":
                    save_format = "zip"
                else:
                    save_format = output_format
                if output_filename == "":
                    output_path = AsposeApp.output_location + Utils.get_filename(Utils(), input_file) + "." + save_format
                else:
                    output_path = AsposeApp.output_location + output_filename + "." + save_format
                Utils.save_file(Utils(), response_stream, output_path)
                return output_path
            else:
                return v_output
        except:
            raise
