
from aspose.cloud.common.product import Product
from aspose.cloud.common.utils import Utils
from aspose.cloud.common.asposeapp import AsposeApp

class SlideConverter(object):
    file_name = ""
    save_format = ""
    def __init__(self, file_name):
        self.file_name = file_name
        self.save_format = "TIFF"
        
    def convert_to_image(self, slide_number, image_format):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/slides/" + self.file_name + "/slides/" + str(slide_number) + "?format=" + image_format
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            output_path = AsposeApp.output_location + Utils.get_filename(Utils(), self.file_name) + "_slide_" + str(slide_number) + "." + image_format
            Utils.save_file(Utils(), response_stream, output_path);
            return output_path
        except:
            raise
    def convert_to_image_by_size(self, slide_number, image_format, width, height):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/slides/" + self.file_name + "/slides/" + str(slide_number) + "?format=" + image_format + "&width=" + str(width) + "&height=" + str(height)
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            output_path = AsposeApp.output_location + Utils.get_filename(Utils(), self.file_name) + "_slide_" + str(slide_number) + "." + image_format
            Utils.save_file(Utils(), response_stream, output_path);
            return output_path
        except:
            raise
        
    def convert(self):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/slides/" + self.file_name + "?format=" + self.save_format
            signed_uri = Utils.sign(self, str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            output_path = AsposeApp.output_location + Utils.get_filename(Utils(), self.file_name) + "." + self.save_format
            Utils.save_file(Utils(), response_stream, output_path);
            return output_path
        except:
            raise
