from aspose.cloud._pyio import open
from aspose.cloud.common import Product, Utils
import json

class OcrExtractor(object):
    
    def extract_text(self, filename, folder=None, language=None, use_default_dictionaries=True, x=None, y=None, width=None, height=None):
        try:
            # build URI            
            if(filename == ""):
                raise "Filename not found."
            
            str_uri_request = Product.base_product_uri + "/ocr/" + filename + "/recognize?"
            if(use_default_dictionaries != None):
                str_uri_request += "useDefaultDictionaries=" + str(use_default_dictionaries)
            
            if(folder != None):
                str_uri_request = str_uri_request + "&folder=" + folder
            
            if(language != None):
                str_uri_request = str_uri_request + "&language=" + language
            
            if(x != None and x > 0):
                str_uri_request = str_uri_request + "&rectX=" + str(x)    
            
            if(y != None and y > 0):
                str_uri_request = str_uri_request + "&rectY=" + str(y)
            
            if(width != None and width > 0):
                str_uri_request = str_uri_request + "&rectWidth=" + str(width)
            
            if(height != None and height > 0):
                str_uri_request = str_uri_request + "&rectHeight=" + str(height)
                
            signed_uri = Utils.sign(Utils(), str_uri_request)
            
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "JSON", "")                       
                        
            json_data = json.loads(response_stream)
            if (json_data["Code"] != 200):
                return False
            else:
                return json_data["Text"]
                    
        except:
            raise
    
    def extract_text_from_local_file(self, local_filename, folder=None, language=None):
        try:
            # build URI            
            if(local_filename == ""):
                raise "Filename not found."
            
            with open(local_filename , "rb") as file_obj:
                file_data = file_obj.read()
                file_obj.close()
                
                        
            
            str_uri_request = Product.base_product_uri + "/ocr/recognize?useDefaultDictionaries=true"
            
            if(folder != None):
                str_uri_request = str_uri_request + "&folder=" + folder
            
            if(language != None):
                str_uri_request = str_uri_request + "&language=" + language
                        
            
            signed_uri = Utils.sign(Utils(), str_uri_request)
            
            response_stream = Utils.process_command(Utils(), signed_uri, "POST", "JSON", file_data)                       
                        
            json_data = json.loads(response_stream)
            
            if (json_data["Code"] != 200):
                return False
            else:
                return json_data["Text"]
                    
        except:
            raise
        
    def extract_text_from_url(self, url, language, use_default_dictionaries):
        try:
            if url == "":
                raise "Please Specify URL"
            str_uri = Product.base_product_uri + "/ocr/recognize?url=" + url + "&language=" + language + "&useDefaultDictionaries" + use_default_dictionaries
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "POST", "", "")
            json_data = json.loads(response_stream)
            return json_data
        except:
            raise
