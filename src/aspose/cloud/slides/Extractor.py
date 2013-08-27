
from aspose.cloud.common.product import Product
from aspose.cloud.common.utils import Utils
import json
class SlideExtractor:
    file_name = ""
    def __init__(self, file_name):
        self.file_name = file_name
        
    def get_image_count(self,storage_type = None,storage_name =None,folder = None):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/slides/" + self.file_name + "/images"
            if folder is not None:
                str_uri += "?folder=" + folder
            if storage_name is not None:
                str_uri += "&storage=" + storage_name
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return len(json_data["Images"]["List"])
            else:
                return json_data
        except:
            raise

    def get_slide_image_count(self, slide_number,storage_type = None,storage_name = None,folder=None):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/slides/" + self.file_name + "/slides/" + str(slide_number) + "/images"
            if folder is not None:
                str_uri += "?folder=" + folder
            if storage_name is not None:
                str_uri += "&storage=" + storage_name
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return len(json_data["Images"]["List"])
            else:
                return json_data
        except:
            raise
    
    def get_shapes(self, slide_number,storage_type = None,storage_name =None,folder=None):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/slides/" + self.file_name + "/slides/" + str(slide_number) + "/shapes"
            if folder is not None:
                str_uri += "?folder=" + folder
            if storage_name is not None:
                str_uri += "&storage=" + storage_name
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            shapes = {}
            if json_data["Code"] == 200:
                shape = {}
                for json_data["ShapeList"]["Links"] in shape:
                    signed_uri = Utils.sign(Utils(), shape["Uri"]["Href"])
                    response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
                    data = json.loads(response_stream)
                    shapes = data
                return shapes
            else:
                return json_data
        except:
            raise
        
    def get_color_scheme(self, slide_number,storage_type = None,storage_name = None):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/slides/" + self.file_name + "/slides/" + str(slide_number) + "/theme/colorScheme"
            if storage_name is not None:
                str_uri += "&storage=" + storage_name
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "" , "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return json_data["ColorScheme"]
            else:
                return json_data
        except:
            raise

    def get_font_scheme(self, slide_number,stroage_type = None,storage_name = None):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/slides/" + self.file_name + "/slides/" + str(slide_number) + "/theme/fontScheme"
            if storage_name is not None:
                str_uri += "&storage=" + storage_name
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return json_data["FontScheme"]
            else:
                return json_data
        except:
            raise
    
    def get_format_scheme(self, slide_number,storage_type = None,storage_name = None):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/slides/" + self.file_name + "/slides/" + str(slide_number) + "/theme/formatScheme"
            if storage_name is not None:
                str_uri += "&storage=" + storage_name
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return json_data["FormatScheme"]
            else:
                return json_data
        except:
            raise

    def get_placeholder_count(self, slide_number,storage_type = None,storage_name = None,folder = None):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/slides/" + self.file_name + "/slides/" + str(slide_number) + "/placeholders"
            if folder is not None:
                str_uri += "?folder=" + folder
            if storage_name is not None:
                str_uri += "&storage=" + storage_name
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return len(json_data["Placeholders"]["PlaceholderLinks"])
            else:
                return json_data
        except:
            raise
            
    def get_placeholder(self, slide_number, placehoder_index,storage_type = None,storage_name= None,folder = None):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/slides/" + self.file_name + "/slides/" + str(slide_number) + "/placeholders/" + str(placehoder_index)
            if folder is not None:
                str_uri += "?folder=" + folder
            if storage_name is not None:
                str_uri += "&storage=" + storage_name
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return json_data["Placeholder"]
            else:
                return json_data
        except:
            raise
