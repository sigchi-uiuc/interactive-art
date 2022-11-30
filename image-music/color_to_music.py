import math
import numpy as np

class Color2Music:
    def __init__(self, rgb, octave=4):
        self.COLOR_MAP = {(82, 0, 0): f"F{octave}", 
                (116, 0, 0): f"F#{octave}", 
                (179, 0, 0): f"G{octave}", 
                (238, 0, 0): f"G#{octave}",
                (255,99,0): f"A{octave}",
                (255, 236, 0): f"A#{octave}",
                (153, 255, 0): f"B{octave}",
                (40, 255, 0): f"C{octave+1}",
                (0, 255, 232): f"C#{octave+1}",
                (0, 124, 255): f"D{octave+1}",
                (5, 0, 255): f"D#{octave+1}",
                (69, 0, 234): f"E{octave+1}",
                (87, 0, 158): f"F{octave+1}"}
        self.rgb = rgb
    
    def get_note(self):
        colors = list(self.COLOR_MAP.keys())
        distances = [self._get_color_dist(color, self.rgb) for color in colors]
        closest_color_idx = np.argmin(np.array(distances))
        return self.COLOR_MAP[colors[closest_color_idx]]
        
    def _get_color_dist(self, rgb1, rgb2):
        return math.sqrt((rgb1[0] - rgb2[0])**2 +  
                        (rgb1[1] - rgb2[1])**2 + 
                        (rgb1[2] - rgb2[2])**2)

