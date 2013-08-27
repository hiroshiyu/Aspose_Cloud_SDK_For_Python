
from aspose.cloud.common.asposeapp import AsposeApp
from aspose.cloud.common.product import Product
from aspose.cloud.common.utils import Utils
import json

class AnnotationEditor(object):
    file_name = ""
    
    def __init__(self, file_name):
        self.file_name = file_name
    
    def get_annotations_count(self, page_number):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/pdf/" + self.file_name + "/pages/" + str(page_number) + "/annotations"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return len(json_data["Annotations"]["List"])
        except:
            raise
        
    def get_annotation(self, page_number, annotation_index):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/pdf/" + self.file_name + "/pages/" + str(page_number) + "/annotations/" + str(annotation_index)
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["Annotation"]
        except:
            raise
        
    def get_all_annotations(self, page_number):    
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            total_annotaions = self.get_annotations_count(page_number)
            list_annotations = {}
            for index in range(1, total_annotaions):
                list_annotations.append(self.get_annotation(page_number, index))
            return list_annotations
        except:
            raise
    
    def get_bookmark_count(self):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/pdf/" + self.file_name + "/bookmarks"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return len(json_data["Bookmarks"]["List"])        
        except:
            raise

    def get_child_bookmark_count(self, parent_index):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/pdf/" + self.file_name + "/bookmarks/" + str(parent_index) + "/bookmarks"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return len(json_data["Bookmarks"]["List"])
        except:
            raise

    def get_bookmark(self, bookmark_index):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/pdf/" + self.file_name + "/bookmarks/" + str(bookmark_index)
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["Bookmark"]
        except:
            raise

    def get_child_bookmark(self, parent_index, child_index):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/pdf/" + self.file_name + "/bookmarks/" + str(parent_index) + "/bookmarks/" + str(child_index)
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["Bookmark"]
        except:
            raise

    def is_child_bookmark(self, bookmark_index):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/pdf/" + self.file_name + "/bookmarks/" + str(bookmark_index)
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["Bookmark"]
        except:
            raise

    def get_all_bookmarks(self):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            total_bookmarks = self.get_bookmark_count()
            list_bookmarks = {}
            for index in range(1, total_bookmarks):
                list_bookmarks.append(self.get_bookmark(index))
            return list_bookmarks
        except:
            raise

    def get_attachments_count(self):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/pdf/" + self.file_name + "/attachments"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return len(json_data["Attachments"]["List"])
        except:
            raise
        
    def get_attachment(self, attachment_index):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/pdf/" + self.file_name + "/attachments/" + str(attachment_index)
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["Attachments"]
        except:
            raise

    def get_all_attachments(self):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            total_attachments = self.get_attachments_count()
            list_attachment = {}
            for index in range(1, total_attachments):
                list_attachment.append(self.get_attachment(index))
            return list_attachment
        except:
            raise

    def download_attachment(self, attachment_index):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            file_information = self.get_attachment(attachment_index)
            str_uri = Product.base_product_uri + "/pdf/" + self.file_name + "/attachments/" + str(attachment_index) + "/download"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            v_output = Utils.validate_output(Utils(), response_stream)
            if v_output == "":
                output_path = AsposeApp.output_location + file_information["Name"]
                Utils.save_file(Utils, response_stream, output_path)
                return output_path
            else:
                return v_output
        except:
            raise

    def get_links_count(self, page_number):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/pdf/" + self.file_name + "/pages/" + str(page_number) + "/links"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["Links"]["List"]
        except:
            raise
        
    def get_link(self, page_number, link_index):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            str_uri = Product.base_product_uri + "/pdf/" + self.file_name + "/pages/" + str(page_number) + "/links/" + str(link_index)
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["Link"]
        except:
            raise
        
    def get_all_link(self, page_number):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            total_links = self.get_links_count(page_number)
            list_links = {}
            for index in range(1, total_links):
                list_links.append(self.get_line(page_number, index))
            return list_links
        except:
            raise

        