import math
import numpy as np

class Color2Music:
    COLOR_MAP = {(82, 0, 0): "F4", 
                (116, 0, 0): "F#4", 
                (179, 0, 0): "G4", 
                (238, 0, 0): "G#4",
                (255,99,0): "A4",
                (255, 236, 0): "A#4",
                (153, 255, 0): "B4",
                (40, 255, 0): "C5",
                (0, 255, 232): "C#5",
                (0, 124, 255): "D5",
                (5, 0, 255): "D#5",
                (69, 0, 234): "E5",
                (87, 0, 158): "F5"}

    def __init__(self, rgb):
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

