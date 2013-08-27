
from aspose.cloud.common.asposeapp import AsposeApp
from aspose.cloud.common.product import Product
from aspose.cloud.common.utils import Utils
import json

class PdfExtractor(object):
    file_name = ""

    def __init__(self, file_name):
        self.file_name = file_name

    def get_image_count(self, page_number):
        try:
            if self.file_name == "":
                raise Exception("Please Specify Pdf File")
            str_uri = Product.base_product_uri + "/pdf/" + self.file_name + "/pages/" + str(page_number) + "/images"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return len(json_data["Images"]["List"])
        except:
            raise

    def get_default_size(self, page_number, image_index, image_format):
        try:
            if self.file_name == "":
                raise Exception("Please Specify Pdf File")
            str_uri = Product.base_product_uri + "/pdf/" + self.file_name + "/pages/" + str(page_number) + "/images/" + str(image_index) + "?format=" + image_format
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            v_output = Utils.validate_output(Utils(), response_stream)
            if v_output == "":
                output_path = AsposeApp.output_location + Utils.get_filename(Utils(), self.file_name) + "_" + str(image_index) + "." + image_format
                Utils.save_file(Utils(), response_stream, output_path)
                return output_path
            else:
                return v_output
        except:
            raise
        
    def get_image_custom_size(self, page_number, image_index, image_format, width, height):
        try:
            if self.file_name == "":
                raise Exception("Please Specify Pdf File")
            str_uri = Product.base_product_uri + "/pdf/" + self.file_name + "/pages/" + str(page_number) + "/images/" + str(image_index) + "?format=" + image_format + "&width=" + str(width) + "&height=" + str(height)
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            v_output = Utils.validate_output(Utils(), response_stream)
            if v_output == "":
                output_path = AsposeApp.output_location + Utils.get_filename(Utils(), self.file_name) + "_" + str(image_index) + "." + image_format
                Utils.save_file(Utils(), response_stream, output_path)
                return output_path
            else:
                return v_output
        except:
            raise
