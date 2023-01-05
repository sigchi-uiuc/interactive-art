from PIL import Image
import colorgram

class ExtractColor:
  def __init__(self, img, num_colors=1):
    self.colors = colorgram.extract(img, num_colors)

  def get_dominant(self):
    return self.colors[0].rgb

  def get_palette(self):
    return [color.rgb for color in self.colors]