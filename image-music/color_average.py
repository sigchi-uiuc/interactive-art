import sys
import subprocess
from colorthief import ColorThief

class ColorAverage:
  def __init__(self, file):
    self.thief = ColorThief(file)
    self.dominant = self.thief.get_color(quality=1)
    self.palette = self.thief.get_palette(quality=1, color_count=5)
  def get_dominant(self):
    return self.dominant
  def get_palette(self):
    return self.palette


