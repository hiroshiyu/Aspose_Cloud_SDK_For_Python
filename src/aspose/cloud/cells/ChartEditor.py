
from aspose.cloud.common.product import Product
from aspose.cloud.common.utils import Utils
from aspose.cloud.storage.folder import Folder
from aspose.cloud.common.asposeapp import AsposeApp
import json

class CellsChartEditor(object):
    file_name = ""
    worksheet_name = ""
    def __init__(self, file_name, worksheet_name):
        self.file_name = file_name
        self.worksheet_name = worksheet_name
    
    def add_chart(self, chart_type, upper_left_row, upper_left_column, lower_right_row, lower_right_column):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify Worksheet Name")
            
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/charts?chartType=" + chart_type + "&upperLeftRow=" + str(upper_left_row) + "&upperLeftColumn=" + str(upper_left_column) + "&lowerRightRow=" + str(lower_right_row) + "&lowerRightColumn=" + str(lower_right_column)
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "PUT", "", "")
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

    def delete_chart(self, chart_index):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify Worksheet Name")
            
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/charts/" + str(chart_index)
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "DELETE", "", "")
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
        
    def get_chart_area(self, chart_index):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify Worksheet Name")
            
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/charts/" + str(chart_index) + "/chartArea"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["ChartArea"]
        except:
            raise

    def get_fill_format(self, chart_index):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify Worksheet Name")
            
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/charts/" + str(chart_index) + "/chartArea/fillFormat"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["FillFormat"]
        except:
            raise
        
    def get_border(self, chart_index):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify Worksheet Name")
            
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/charts/" + str(chart_index) + "/chartArea/border"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["Line"]
        except:
            raise
