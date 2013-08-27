
from aspose.cloud.common import *
import os
import json


class Folder:
    str_uri_folder = "";
    str_uri_file = "";
    str_uri_exist = "";
    str_uri_disc = "";
    
    def __init__(self):
        self.str_uri_folder = Product.base_product_uri + "/storage/folder";
        self.str_uri_file = Product.base_product_uri + "/storage/file/";
        self.str_uri_exist = Product.base_product_uri + "/storage/exist/";
        self.str_uri_disc = Product.base_product_uri + "/storage/disc";
    
    def get_folders(self):
        try:
            # build URI
            str_uri_request = self.str_uri_folder
            signed_uri = Utils.sign(Utils(), str_uri_request)
            
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "JSON", "")                       
                        
            json_data = json.loads(response_stream)
            
            if (json_data['Code'] != 200):
                return False
            else:
                return response_stream
                    
        except:
            raise
        
    def create_folder(self, str_folder, storage_type=None, storage_name=None):
        try:
            # build URI
            str_uri_request = self.str_uri_folder + '/' + str_folder
            
            if storage_name is not None:
                str_uri_request += "?storage=" + storage_name
            signed_uri = Utils.sign(Utils(), str_uri_request)

            response_stream = Utils.process_command(Utils(), signed_uri, "PUT", "", "")
            
            return response_stream
                    
        except:
            raise 
        
    def get_space_info(self):
        try:
                    # build URI
            str_uri = self.str_uri_disc
                
            # sign URI
            signed_uri = Utils.sign(Utils(), str_uri);
             
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "JSON", "")
            
            return response_stream
            
            
        except:
            raise
    
    def upload_file(self, str_file, str_folder, storage_type=None, storage_name=None):
        try:
            str_remote_filename = os.path.basename(str_file);
            str_uri_request = self.str_uri_file;
                
            if str_folder == "":
                str_uri_request += str_remote_filename;
            else:
                str_uri_request += str_folder + "/" + str_remote_filename;
            if storage_name is not None:
                str_uri_request += "?storage=" + storage_name
            signed_uri = Utils.sign(Utils(), str_uri_request);
            Utils.upload_file_binary(Utils(), signed_uri, str_file, "json");
        
        except:
            raise 
        
    def file_exists(self, filename, storage_type=None, storage_name=None):
        try:
            if filename == "":
                raise Exception("No file name specified")
                
            # build URI
            str_uri = self.str_uri_exist + filename
            if storage_name is not None:
                str_uri += "?storage=" + storage_name
            # sign URI
            signed_uri = Utils.sign(Utils(), str_uri)
             
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "JSON", "")
            
            return response_stream
            
            
        except:
            raise
        
    
    def get_file(self, file_name,storage_type=None,storage_name=None):
        try:
            if file_name == "":
                raise Exception("No file name specified")
            str_uri = self.str_uri_file + file_name
            if storage_name is not None:
                str_uri += "?storage=" + storage_name
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "JSON", "")
            return response_stream
        except:
            raise
   
# Deletes a file from aspose.cloud.remote storage
#
# @param string $filename
#
    def delete_file(self, filename, storage_type=None, storage_name=None):
    
        try:
        
            # //check whether file is set or not
            if (filename == ""):
                raise Exception("No file name specified");
             
            # build URI
            str_uri = self.str_uri_file + filename
             
            if storage_name is not None:
                str_uri += "?storage=" + storage_name
            # sign URI
            signed_uri = Utils.sign(str_uri);
             
            response_stream = json.loads(Utils.process_command(signed_uri, "DELETE", "", ""));
                        
            if (response_stream['Code'] != 200):
                return False;
            else:
                return True
             
        except:
            raise 
        
    def delete_folder(self, folder_name):
        try:
            if folder_name == "":
                raise Exception("No File Name specified")
            str_uri = self.str_uri_folder + folder_name
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = json.loads(Utils.process_command(Utils(), signed_uri, "DELETE", "", ""))
            if response_stream["Code"] != 200:
                return False
            else:
                return True
        except:
            raise
    def get_disc_usage(self, storage_type=None, storage_name=None):
        try:
            str_uri = self.str_uri_disc
            if storage_name is not None:
                str_uri += "?storage=" + storage_name
            signed_uri = Utils.sign(Utils(), str_uri)
            response_string = json.loads(Utils.process_command(Utils(), signed_uri, "GET", "", ""))
            return response_string["DiscUsage"]
        except:
            raise
    def get_file_list(self,str_folder,storage_type=None,storage_name=None):
        try:
            str_uri = self.str_uri_folder
            
            if storage_name is not None:
                str_uri += "?storage=" + storage_name
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json = json.loads(response_stream)
            return json["Files"]
        except:
            raise