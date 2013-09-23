from aspose.cloud.common.asposeapp import AsposeApp
from aspose.cloud.common.product import Product
from aspose.cloud.common.utils import Utils
from aspose.cloud.storage.folder import Folder
import json

class PdfDocument(object):
    file_name = ""
    def __init__(self, file_name):
        self.file_name = file_name
    
    def get_page_count(self):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/pdf/" + self.file_name + "/pages"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return len(json_data["Pages"]["List"])
        except:
            raise
            
    def append_document(self, base_pdf, new_pdf, start_page=0, end_page=0, source_folder=""):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if base_pdf == "":
                raise Exception("Please Specify Base File Name")
            if new_pdf == "":
                raise Exception("Please Specify New Pdf File Name")
            if source_folder == "":
                str_uri = Product.base_product_uri + "/pdf/" + base_pdf + "/appendDocument?appendFile=" + new_pdf
                if start_page > 0:
                    str_uri += "&startPage=" + str(start_page)
                if end_page > 0:
                    str_uri += "&endPage=" + str(end_page) 
            else:
                str_uri = Product.base_product_uri + "/pdf/" + base_pdf + "/appendDocument?appendFile=" + new_pdf
                if not start_page.empty:
                    str_uri += "&startPage=" + str(start_page)
                if not end_page.empty:
                    str_uri += "&endPage=" + str(end_page) 
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "POST", "", "")
            v_output = Utils.validate_output(Utils(), response_stream)
            if v_output == "":
    folder_obj = Folder()
    if source_folder == "":
     output_stream = folder_obj.get_file(base_pdf) 
    else:
     output_stream = folder_obj.get_file(source_folder + "/" + base_pdf)
    output_path = AsposeApp.output_location + base_pdf
    Utils.save_file(Utils(), output_stream, output_path)
    return output_path
            else:
                return v_output
        except:
            raise

    def merge_documents(self, source_files=[]):
        try:
            merged_filename = self.file_name
            if merged_filename == "":
                raise Exception("Output File Not Specified")
            if not source_files:
                raise Exception("Files To Merge Are Not Specified")
            if len(source_files) < 2:
                raise Exception("Two or More Files Are Requred to Merge")
            document_list = {"List" : source_files}
            json_decode = json.dumps(document_list)
            str_uri = Product.base_product_uri + "/pdf/" + merged_filename + "/merge"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "PUT", "JSON", json_decode)
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return True
            else:
                return False
        except:
            raise

    def create_from_html(self, pdf_filename, html_filename):
        try:
            if pdf_filename == "":
                raise Exception("PDF file Name Not Specified")
            if html_filename == "":
                raise Exception("HTML Template File Name Not Specified")
            str_uri = Product.base_product_uri + "/pdf/" + pdf_filename + "?templateFile=" + html_filename + "&templateType=html"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "PUT", "", "")
            v_output = Utils.validate_output(Utils(), response_stream)
            if v_output == "":
                folder = Folder()
                output_stream = folder.get_file(pdf_filename)
                output_path = AsposeApp.output_location + pdf_filename
                Utils.save_file(Utils(), output_stream, output_path)
                return output_path
            else:
                return v_output
        except:
            raise 

    def create_from_xml(self, pdf_filename, xslt_filename, xml_filename):
        try:
            if pdf_filename == "":
                raise Exception("PDF File Name Not Specified")
            if xslt_filename == "":
                raise Exception("XSLT File Name Not Specified")
            if xml_filename == "":
                raise Exception("XML File Name Not Specified")
            str_uri = Product.base_product_uri + "/pdf/" + pdf_filename + "?templateFile=" + xslt_filename + "&dataFile=" + xml_filename + "&templateType=xml"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "PUT", "", "")
            v_output = Utils.validate_output(Utils(), response_stream)
            if v_output == "":
                folder = Folder()
                output_stream = folder.get_file(pdf_filename)
                output_path = AsposeApp.output_location + pdf_filename
                Utils.save_file(Utils(), output_stream, output_path)
                return output_path
            else:
                return v_output
        except:
            raise

    def get_formfield_count(self):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/pdf/" + self.file_name + "/fields"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return len(json_data["Fields"]["List"])
        except:
            raise

    def get_formfields(self):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/pdf/" + self.file_name + "/fields"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["Fields"]["List"]
        except:
            raise
        
    def get_formfield(self, field_name):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/pdf/" + self.file_name + "/fields/" + field_name
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["Field"]
        except:
            raise
    
    def create_empty_pdf(self, pdf_filename):
        try:
            if pdf_filename == "":
                raise Exception("Please Specify PDF file name")
            str_uri = Product.base_product_uri + "/pdf/" + pdf_filename
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "PUT", "", "")
            v_output = Utils.validate_output(Utils(), response_stream)
            if v_output == "":
                folder = Folder()
                output_stream = folder.get_file(pdf_filename)
                output_path = AsposeApp.output_location + pdf_filename
                Utils.save_file(Utils(), output_stream, output_path)
                return output_path
            else:
                return v_output
        except:
            raise
    
    def add_new_page(self):
        try:
            if self.file_name == "":
                raise Exception("Please Specify Pdf File Name")
            str_uri = Product.base_product_uri + "/pdf/" + self.file_name + "/pages"
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

    def delete_page(self, page_number):
        try:
            if self.file_name == "":
                raise Exception("Please Specify Pdf File Name")
            str_uri = Product.base_product_uri + "/pdf/" + self.file_name + "/pages/" + str(page_number)
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
        
    def move_page(self, page_number, new_location):
        try:
            if self.file_name == "":
                raise Exception("Please Specify Pdf File Name")
            str_uri = Product.base_product_uri + "/pdf/" + self.file_name + "/pages/" + str(page_number) + "/movePage?newIndex=" + str(new_location)
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "POST", "", "")
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

    def replace_image_using_stream(self, page_number, image_index, image_stream):
        try:
            if self.file_name == "":
                raise Exception("Please Specify Pdf File Name")
            str_uri = Product.base_product_uri + "/pdf/" + self.file_name + "/pages/" + str(page_number) + "/images/" + str(image_index)
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "POST", "", image_stream)
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

    def replace_image_using_file(self, page_number, image_index, file_name):
        try:
            if self.file_name == "":
                raise Exception("Please Specify Pdf File Name")
            str_uri = Product.base_product_uri + "/pdf/" + self.file_name + "/pages/" + str(page_number) + "/images/" + str(image_index) + "?imageFile=" + file_name
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "POST", "", "")
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

    def get_document_properties(self):
        try:
            if self.file_name == "":
                raise Exception("Please Specify Pdf File Name")
            str_uri = Product.base_product_uri + "/pdf/" + self.file_name + "/documentProperties"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["DocumentProperties"]["List"]
        except:
            raise
            
    def get_document_property(self, property_name):
        try:
            if self.file_name == "":
                raise Exception("Please Specify Pdf File Name")
            if property_name == "":
                raise Exception("Please Specify Property Name")
            str_uri = Product.base_product_uri + "/pdf/" + self.file_name + "/documentProperties/" + property_name
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["DocumentProperty"]
        except:
            raise 

    def set_document_property(self, property_name, property_value):
        try:
            if self.file_name == "":
                raise Exception("Please Specify Pdf File Name")
            if property_name == "":
                raise Exception("Please Specify Property Name")
            
            str_uri = Product.base_product_uri + "/pdf/" + self.file_name + "/documentProperties/" + property_name
            put_arr = {"Value" : property_value}
            json_arr = json.dumps(put_arr)
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "PUT", "JSON", json_arr)
            json_data = json.loads(response_stream)
            return json_data["DocumentProperty"]
        except:
            raise
    
    def remove_all_properties(self):
        try:
            if self.file_name == "":
                raise Exception("Please Specify Pdf File Name")
            str_uri = Product.base_product_uri + "/pdf/" + self.file_name + "/documentProperties"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "DELETE", "", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return True
            else:
                return False
        except:
            raise
