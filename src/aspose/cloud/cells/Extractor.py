
from aspose.cloud.common.product import Product
from aspose.cloud.common.utils import Utils
from aspose.cloud.common.asposeapp import AsposeApp

class CellsExtractor(object):

    file_name = ""
    def __init__(self, file_name):
        self.file_name = file_name
        
    def get_picture(self, worksheet_name, picture_index, image_format):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + worksheet_name + "/pictures/" + str(picture_index) + "?format=" + image_format
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

    def get_oleobject(self, worksheet_name, oleobject_index, image_format):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + worksheet_name + "/oleobjects/" + str(oleobject_index) + "?format=" + image_format
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
        
    def get_chart(self, worksheet_name, chart_index, image_format):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + worksheet_name + "/charts/" + str(chart_index) + "?format=" + image_format
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
        
    def get_autoshape(self, worksheet_name, autoshape_index, image_format):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + worksheet_name + "/autoshapes/" + str(autoshape_index) + "?format=" + image_format
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