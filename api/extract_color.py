import colorgram
from PIL import ImageStat

class ExtractColor:
  def __init__(self, img, num_colors=1):
    self.colors = colorgram.extract(img, num_colors)
  
  def get_dominant(self):
    return self.colors[0].rgb
  
  def get_palette(self):
    return [color.rgb for color in self.colors]
  
  @staticmethod
  def get_luminance(img):
    img_grey = img.convert('L')
    stat = ImageStat.Stat(img_grey)
    bright = stat.mean[0]
    return bright