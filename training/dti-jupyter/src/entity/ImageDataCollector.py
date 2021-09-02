import io
import numpy as np
import urllib
from PIL import Image


def get_metadata_from_url(input_url):
    
    pil_im = None
    ## start request the image ##
    with urllib.request.urlopen(cat1_IDC.blob_url) as url:
        temp_img = url.read()
        pil_im = Image.open(io.BytesIO(temp_img), 'r')
    ## assign the image info into the C3 Type ##
    self.image_width, self.image_height = pil_im.size

    return -1
