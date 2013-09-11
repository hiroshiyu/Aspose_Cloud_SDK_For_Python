
from aspose.cloud.common.product import Product
from aspose.cloud.common.utils import Utils
import json

class Worksheet(object):
    file_name = ""
    worksheet_name = ""
    def __init__(self, file_name, worksheet_name):
        self.file_name = file_name
        self.worksheet_name = worksheet_name
        
    def get_cells_list(self, off_set, count):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify worksheet Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/cells?offset=" + str(off_set) + "&count=" + str(count)
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["Cells"]["CellList"]
        except:
            raise
        
    def get_row_list(self):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify worksheet Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/cells/rows"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["Rows"]["RowsList"]
        except:
            raise
        
    def get_column_list(self):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify worksheet Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/cells/columns"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["Columns"]["ColumnsList"]
        except:
            raise
        
    def get_max_column(self, off_set, count):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify worksheet Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/cells?offset=" + str(off_set) + "&count=" + str(count)
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["Cells"]["MaxColumn"]
        except:
            raise
        
    def get_max_row(self, off_set, count):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify worksheet Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/cells?offset=" + str(off_set) + "&count=" + str(count)
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["Cells"]["MaxRow"]
        except:
            raise
        
    def get_cells_count(self, off_set, count):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify worksheet Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/cells?offset=" + str(off_set) + "&count=" + str(count)
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["Cells"]["CellCount"]
        except:
            raise
    
    def get_autoshapes_count(self):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify worksheet Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/autoshapes"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return len(json_data["AutoShapes"]["AutoShapeList"])
        except:
            raise
        
    def get_autoshape_byindex(self, index):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify worksheet Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/autoshapes/" + str(index)
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["AutoShape"]
        except:
            raise

    def get_charts_count(self):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify worksheet Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/charts"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return len(json_data["Charts"]["ChartList"])
        except:
            raise
        
    def get_chart_byindex(self, index):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify worksheet Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/charts/" + str(index)
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["Chart"]
        except:
            raise

    def get_hyperlinks_count(self):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify worksheet Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/hyperlinks"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return len(json_data["Hyperlinks"]["HyperlinkList"])
        except:
            raise

    def get_hyperlink_byindex(self, index):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify worksheet Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/hyperlinks/" + str(index) 
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["Hyperlink"]
        except:
            raise

    def get_comment(self, cell_name):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify worksheet Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/comments/" + cell_name
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["Comment"]["HtmlNote"]
        except:
            raise

    def get_oleobject_byindex(self, index):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify worksheet Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/oleobjects/" + str(index) 
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["OleObject"]
        except:
            raise
        
    def get_picture_byindex(self, index):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify worksheet Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/pictures/" + str(index) 
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["Picture"]
        except:
            raise

    def get_validation_byindex(self, index):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify worksheet Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/validations/" + str(index) 
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["Validation"]
        except:
            raise
        
    def get_mergedcell_byindex(self, index):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify worksheet Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/mergedCells/" + str(index) 
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["MergedCell"]
        except:
            raise

    def get_mergedcell_count(self):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify worksheet Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/mergedCells"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["MergedCells"]["Count"]
        except:
            raise
        
    def get_validations_count(self):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify worksheet Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/validations"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["Validations"]["Count"]
        except:
            raise
        
    def get_pictures_count(self):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify worksheet Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/pictures"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return len(json_data["Pictures"]["PictureList"])
        except:
            raise

    def get_oleobjects_count(self):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify worksheet Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/oleobjects"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return len(json_data["OleObjects"]["OleObjectList"])
        except:
            raise
        
    def get_comments_count(self):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify worksheet Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/comments"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return len(json_data["Comments"]["CommentList"])
        except:
            raise

    def hide_worksheet(self):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify worksheet Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/visible?isVisible=false"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "PUT", "", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return True
            else:
                return False
        except:
            raise
    
    def unhide_worksheet(self):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify worksheet Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/visible?isVisible=true"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "PUT", "", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return True
            else:
                return False
        except:
            raise

    def move_worksheet(self, worksheet_name, position):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify worksheet Name")
            post_data = {"DestinationWorsheet" : worksheet_name, "Position" : position}
            json_arr = json.dumps(post_data)
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/position"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "POST", "json", json_arr)
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return True
            else:
                return False
        except:
            raise

    def calculate_formula(self, formula):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify worksheet Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/formulaResult?formula=" + formula
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["Value"]["Value"]
        except:
            raise

    def set_cell_value(self, cell_name, value_type, value):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify worksheet Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/cells/" + cell_name + "?value=" + str(value) + "&type=" + value_type
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "POST", "", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return True
            else:
                return False
        except:
            raise

    def get_rows_count(self, off_set, count):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify worksheet Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/cells/rows?offset=" + str(off_set) + "&count=" + str(count)
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["Rows"]["RowsCount"]
        except:
            raise
        
    def get_rows(self, row_index):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify worksheet Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/cells/rows/" + str(row_index)
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["Row"]
        except:
            raise
        
    def delete_rows(self, row_index):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify worksheet Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/cells/rows/" + str(row_index)
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "DELETE", "", "")
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return True
            else:
                return False
        except:
            raise
        
    def get_column(self, column_index):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify worksheet Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/cells/columns/" + str(column_index)
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["Column"]
        except:
            raise

    def sort_data(self, cell_area, data_sort={}):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify worksheet Name")
            json_arr = json.dumps(data_sort)
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/sort?cellArea=" + cell_area
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "POST", "json", json_arr)
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return True
            else:
                return False
        except:
            raise
        
    def set_cell_style(self, cell_name, style={}):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify Worksheet Name")
            json_arr = json.dumps(style)
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/cells/" + cell_name + "/style"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "POST", "json", json_arr)
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200:
                return True
            else:
                return False
        except:
            raise

    def get_cell(self, cell_name):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.woksheet_name == "":
                raise Exception("Please Specify worksheet Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/cells/" + cell_name
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data["Cell"]
        except:
            raise
    
    def get_cell_style(self, cell_name):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.worksheet_name == "":
                raise Exception("Please Specify Worksheet Name")
            str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/cells/" + cell_name + "/style"
            signed_uri = Utils.sign(Utils(), str_uri)
            response_stream = Utils.process_command(Utils(), signed_uri, "GET", "", "")
            json_data = json.loads(response_stream)
            return json_data
        except:
            raise
        
    def add_picture(self, picture_path, picture_location, upper_left_row=None, upper_left_column=None, lower_right_row=None, lower_right_column=None):
        try:
            if self.file_name == "":
                raise Exception("Please Specify File Name")
            if self.workseet_name == "":
                raise Exception("Please Specify File Name")
            if picture_location == "Server" or picture_location == "server":
                str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/pictures?upperLeftRow=" + str(upper_left_row) + "&upperLeftColumn=" + str(upper_left_column) + "&lowerRightRow=" + str(lower_right_row) + "&lowerRightColumn=" + str(lower_right_column) + "&picturePath=" + picture_path
                signed_uri = Utils.sign(Utils(), str_uri)
                response_stream = Utils.process_command(Utils(), signed_uri, "PUT", "", "")
            elif picture_location == "Local" or picture_location == "local":
                stream = open(picture_path).read()
                str_uri = Product.base_product_uri + "/cells/" + self.file_name + "/worksheets/" + self.worksheet_name + "/pictures?upperLeftRow=" + str(upper_left_row) + "&upperLeftColumn=" + str(upper_left_column) + "&lowerRightRow=" + str(lower_right_row) + "&lowerRightColumn=" + str(lower_right_column)
                signed_uri = Utils.sign(Utils(), str_uri)
                response_stream = Utils.process_command(Utils(), signed_uri, "PUT", "JSON", stream)
            json_data = json.loads(response_stream)
            if json_data["Code"] == 200 :
                return True
            else:
                return False
            
        except:
            raise
