
from aspose.cloud.common.product import Product
from aspose.cloud.common.utils import Utils
from aspose.cloud.common.asposeapp import AsposeApp
class BarcodeBuilder(object):
   
    def save(self, codeText, symbology, imageFormat, xResolution, yResolution, xDimension, yDimension):
        strURI = Product.base_product_uri + "/barcode/generate?text=" + codeText + "&type=" + str(symbology) + "&format=" + imageFormat
        if xResolution <= 0:
            strURI += ""
        else:
            strURI += "&resolutionX=" + str(xResolution)
        if yResolution <= 0:
            strURI += ""
        else:
            strURI += "&resolutionY=" + str(yResolution)
        if xDimension <= 0:
            strURI += ""
        else:
            strURI += "&dimensionX=" + str(xDimension)
        if yDimension <= 0:
            strURI += ""
        else:
            strURI += "&dimensionY=" + str(yDimension)
        try:
            signedURI = Utils.sign(Utils(), strURI)
            response = Utils.process_command(Utils(), signedURI, "GET", "", "")
            v_output = Utils.validate_output(self, response)
            if(v_output == ""):
                output_path = AsposeApp.output_location + "barcode" + str(symbology) + "." + imageFormat
                Utils.save_file(self, response, output_path)
                return output_path
        except:
            raise
