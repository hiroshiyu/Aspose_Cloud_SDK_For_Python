
import json
from aspose.cloud.common.product import Product
from aspose.cloud.common.utils import Utils
from aspose.cloud.storage.folder import Folder
from aspose.cloud.common.asposeapp import AsposeApp

class WordDocumentBuilder(object):
    
    
    def insert_watermark_text(self, file_name, text, rotation_angle):
        try:
            if file_name == "":
                raise Exception("Please Specify File Name")
            field_array = {"Text" : text, "RotationAngle" : str(rotation_angle)}
            json_post_data = json.dumps(field_array)
            str_uri = Product.base_product_uri + "/words/" + file_name + "/insertWatermarkText"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "POST", "json", json_post_data)
            v_output = Utils.validate_output(Utils(), response_stream)
            if v_output == "":
                folder = Folder()
                output_stream = folder.get_file(file_name)
                output_path = AsposeApp.output_location + file_name
                Utils.save_file(Utils(), output_stream, output_path)
                return output_path
            else:
                return v_output
        except:
            raise

    def insert_watermark_image(self, file_name, image_filename, rotation_angle):
        try:
            if file_name == "":
                raise Exception("Please Specify File Name")
            if image_filename == "":
                raise Exception("Please Specify Image File Name")
            str_uri = Product.base_product_uri + "/words/" + file_name + "/insertWatermarkImage?imageFile=" + image_filename + "&rotationAngle=" + str(rotation_angle)
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "POST", "json", "")
            v_output = Utils.validate_output(Utils(), response_stream)
            if v_output == "":
                folder = Folder()
                output_stream = folder.get_file(file_name)
                output_path = AsposeApp.output_location + file_name
                Utils.save_file(Utils(), output_stream, output_path)
                return output_path
            else:
                return v_output
        except:
            raise

    def replace_text(self, file_name, old_value, new_value, is_match_case, is_match_whole_word):
        try:
            if file_name == "":
                raise Exception("Please Specify File Name")
            field_arr = {"OldValue" : old_value, "NewValue" : new_value, "IsMatchCase" : str(is_match_case), "IsMatchWholeWord" : str(is_match_whole_word)}
            json_arr = json.dumps(field_arr)
            str_uri = Product.base_product_uri + "/words/" + file_name + "/replaceText"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "POST", "json", json_arr)
            v_output = Utils.validate_output(Utils(), response_stream)
            if v_output == "":
                folder = Folder()
                output_stream = folder.get_file(file_name)
                output_path = AsposeApp.output_location + file_name
                Utils.save_file(Utils(), output_stream, output_path)
                return output_path
            else:
                return v_output
        except:
            raise
