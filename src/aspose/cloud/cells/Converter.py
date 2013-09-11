from aspose.cloud.common.product import Product
from aspose.cloud.common.utils import Utils
from aspose.cloud.common.asposeapp import AsposeApp

class CellsConverter(object):
    file_name = ""
    worksheet_name = ""
    save_format = ""

    def __init__(self, *args):
        num_of_args = len(args)
        if num_of_args == 1:
            self.file_name = args[0]
        elif num_of_args == 2:
            self.file_name = args[0]
            self.worksheet_name = args[1]
        else:
            raise Exception("Wrong Numbers of Arguments")
        self.save_format = "xls"
    
    def convert(self):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "?format=" + self.save_format
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            v_output = Utils.validate_output(Utils(), response_stream)
            if v_output == "":
                output_path = AsposeApp.output_location + Utils.get_filename(Utils(), self.file_name) + "." + self.save_format
                Utils.save_file(Utils(), response_stream, output_path)
                return output_path
            else:
                return v_output
        except:
            raise

    def convert_to_image(self, image_format, worksheet_name):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + worksheet_name + "?format=" + image_format
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            v_output = Utils.validate_output(Utils(), response_stream)
            if v_output == "":
                output_path = AsposeApp.output_location + Utils.get_filename(Utils(), self.file_name) + "_" + worksheet_name + "." + image_format
                Utils.save_file(Utils(), response_stream, output_path)
                return output_path
            else:
                return v_output
        except:
            raise

    def save(self, output_format):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "?format=" + output_format
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            v_output = Utils.validate_output(Utils(), response_stream)
            if v_output == "":
                output_path = AsposeApp.output_location + Utils.get_filename(Utils(), self.file_name) + "." + output_format
                Utils.save_file(Utils(), response_stream, output_path)
                return output_path
            else:
                return v_output
        except:
            raise
        
    def worksheet_to_image(self, image_format):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify Worksheet")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "?format=" + image_format
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            v_output = Utils.validate_output(Utils(), response_stream)
            if v_output == "":
                output_path = AsposeApp.output_location + Utils.get_filename(Utils(), self.file_name) + "_" + self.worksheet_name + "." + image_format
                Utils.save_file(Utils(), response_stream, output_path)
                return output_path
            else:
                return v_output
        except:
            raise
        
    def picture_to_image(self, picture_index, image_format):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify Worksheet")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/pictures/" + str(picture_index) + "?format=" + image_format
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            v_output = Utils.validate_output(Utils(), response_stream)
            if v_output == "":
                output_path = AsposeApp.output_location + Utils.get_filename(Utils(), self.file_name) + "_" + self.worksheet_name + "." + image_format
                Utils.save_file(Utils(), response_stream, output_path)
                return output_path
            else:
                return v_output
        except:
            raise

    def oleobject_to_image(self, oleobject_index, image_format):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify Worksheet")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/oleobjects/" + str(oleobject_index) + "?format=" + image_format
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            v_output = Utils.validate_output(Utils(), response_stream)
            if v_output == "":
                output_path = AsposeApp.output_location + Utils.get_filename(Utils(), self.file_name) + "_" + self.worksheet_name + "." + image_format
                Utils.save_file(Utils(), response_stream, output_path)
                return output_path
            else:
                return v_output
        except:
            raise
        
    def chart_to_image(self, chart_index, image_format):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify Worksheet")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/charts/" + str(chart_index) + "?format=" + image_format
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            v_output = Utils.validate_output(Utils(), response_stream)
            if v_output == "":
                output_path = AsposeApp.output_location + Utils.get_filename(Utils(), self.file_name) + "_" + self.worksheet_name + "." + image_format
                Utils.save_file(Utils(), response_stream, output_path)
                return output_path
            else:
                return v_output
        except:
            raise
        
    def autoshape_to_image(self, shape_index, image_format):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify Worksheet")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/autoshapes/" + str(shape_index) + "?format=" + image_format
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            v_output = Utils.validate_output(Utils(), response_stream)
            if v_output == "":
                output_path = AsposeApp.output_location + Utils.get_filename(Utils(), self.file_name) + "_" + self.worksheet_name + "." + image_format
                Utils.save_file(Utils(), response_stream, output_path)
                return output_path
            else:
                return v_output
        except:
            raise
