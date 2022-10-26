from colorthief import ColorThief
from PIL import Image
import os

class ExtractColor:
  def __init__(self, img, section_num, data_dir):
    # load file
    f_name = os.path.join(data_dir, str(section_num) + ".jpg")
    img.save(f_name)
    self.thief = ColorThief(f_name)

    # get dominant colors
    self.dominant = self.thief.get_color(quality=1)
    self.palette = self.thief.get_palette(quality=1, color_count=5)

    # remove tmp file
    os.remove(f_name)

  def get_dominant(self):
    # color = Image.new('RGB', (200,200), self.dominant)
    # color.show()
    return self.dominant
  def get_palette(self):
    return self.palette


