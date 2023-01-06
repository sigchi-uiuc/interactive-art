from PIL import Image
from process_image import SplitImage
import colorgram

class ExtractColor:
  def __init__(self, img_file, num_sections):
    self.img = Image.open(img_file)
    self.split = SplitImage(self.img.size, num_sections)
  
  def get_color_sections(self, num_colors=1):
    colors = []
    for chunk in self.split.get_chunks():
       image_section = self.img.crop(chunk)

       color_section = colorgram.extract(image_section, num_colors)
       dominant_color = color_section[0].rgb
       colors.append(dominant_color) 

    return colors