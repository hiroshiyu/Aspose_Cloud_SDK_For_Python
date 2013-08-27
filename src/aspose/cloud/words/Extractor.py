
from aspose.cloud.common.product import Product
from aspose.cloud.common.utils import Utils
import json
from aspose.cloud.common.asposeapp import AsposeApp

class WordExtractor(object):
    file_name = ""
    def __init__(self, file_name):
        self.file_name = file_name
    
    def get_text(self):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/words/" + self.file_name + "/textItems"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return json_data["TextItems"]["List"]
            else:
                return False
        except:
            raise
    
    def get_oleobject(self, index, output_format):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/words/" + self.file_name + "/drawingObjects/" + str(index) + "/oleData"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            v_output = Utils.validate_output(Utils(), response_stream)
            if v_output == "":
                output_path = AsposeApp.output_location + Utils.get_filename(Utils(), self.file_name) + "_" + str(index) + "." + output_format
                Utils.save_file(Utils(), response_stream, output_path)
                return output_path
            else:
                return v_output
        except:
            raise

    def get_image_data(self, index, render_format):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/words/" + self.file_name + "/drawingObjects/" + str(index) + "/ImageData"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            v_output = Utils.validate_output(Utils(), response_stream)
            if v_output == "":
                output_path = AsposeApp.output_location + Utils.get_filename(Utils(), self.file_name) + "_" + str(index) + "." + render_format
                Utils.save_file(Utils(), response_stream, output_path)
                return output_path
            else:
                return v_output
        except:
            raise
        
    def convert_drawing_object(self, index, render_format):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/words/" + self.file_name + "/drawingObjects/" + str(index) + "?format=" + render_format
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            v_output = Utils.validate_output(Utils(), response_stream)
            if v_output == "":
                output_path = AsposeApp.output_location + Utils.get_filename(Utils(), self.file_name) + "_" + str(index) + "." + render_format
                Utils.save_file(Utils(), response_stream, output_path)
                return output_path
            else:
                return v_output
        except:
            raise
        
    def get_drawing_objects_list(self):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/words/" + self.file_name + "/drawingObjects"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return json_data["DrawingObjects"]["List"]
            else:
                return False
        except:
            raise

    def get_drawing_object(self, object_uri, output_path):
        
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if object_uri == "":
                raise Exception("Please Specify Object URI")
            if output_path == "":
                raise Exception("Please Specify Output Path")
            
            url_arr = object_uri.split("/")
            object_index = self.end(url_arr) 
            str_uri = object_uri
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                if json_data["DrawingObject"]["ImageDataLink"] != "":
                    str_uri = str_uri + "/imageData"
                    output_path = output_path + "\\DrawingObject_" + str(object_index) + ".jpeg"
                elif json_data["DrawingObject"]["OLEDataLink"] != "":
                    str_uri = str_uri + "/oleData"
                    output_path = output_path + "\\DrawingObject_" + str(object_index) + ".xlsx"
                else:
                    str_uri = str_uri + "?format=jpeg"
                    output_path = output_path + "\\DrawingObject_" + str(object_index) + ".jpeg"
                signed_uri = Utils.sign(Utils(), str_uri)
                response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
                v_output = Utils.validate_output(Utils(), response_stream)
                if v_output == "":
                    Utils.save_file(Utils(), response_stream, output_path)
                    return output_path
                else:
                    return v_output
            else:
                return False
        except:
            raise

    def get_drawing_objects(self, output_path):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if output_path == "":
                raise Exception("Please Specify Output File Path")
            str_uri = Product.base_product_uri + "/words/" + self.file_name + "/drawingObjects"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                for item in json_data["DrawingObjects"]["List"]:
                    self.get_drawing_object(item["link"]["Href"], output_path)
            else:
                return False
        except:
            raise
            
    def end(self, tmp):
        return tmp[-1]        
