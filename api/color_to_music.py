import math
import numpy as np
from util import convert_range

class Color2Music:
    MAX_BPM = 80
    MIN_BPM = 40
    MIN_OCTAVE = 3
    MAX_OCTAVE = 5

    def __init__(self, rgb, octave=4):
        self.CHORDS = {"Cmajor": [f"C{octave}", f"E{octave}", f"G{octave}"],
                      "Gmajor": [f"G{octave}", f"B{octave}", f"D{octave}"],
                      "Dmajor": [f"D{octave}", f"F#{octave}", f"A{octave}"],
                      "Amajor": [f"A{octave}", f"C#{octave}", f"E{octave}"],
                      "Emajor": [f"E{octave}", f"G#{octave}", f"B{octave}"],
                      "Bmajor": [f"B{octave}", f"D#{octave}", f"F#{octave}"],
                      "F#minor": [f"F#{octave}", f"A{octave}", f"C#{octave}"], 
                      "Dbminor": [f"C#{octave}", f"E{octave}", f"G#{octave}"], 
                      "Abminor": [f"G#{octave}", f"B{octave}", f"D#{octave}"], 
                      "Ebminor": [f"D#{octave}", f"F#{octave}", f"A#{octave}"], 
                      "Bbminor": [f"A#{octave}", f"C#{octave}", f"F{octave}"], 
                      "Fminor": [f"F{octave}", f"G#{octave}", f"C{octave}"]} 

        self.COLOR_MAP = {(255, 0, 0): self.CHORDS['Cmajor'], #red
                          (255, 128, 0): self.CHORDS['Gmajor'], #orange
                          (255, 255, 0): self.CHORDS['Dmajor'], #yellow
                          (47, 205, 48): self.CHORDS['Amajor'], #green
                          (196, 242, 255): self.CHORDS['Emajor'], #light blue
                          (143, 202, 255): self.CHORDS['Bmajor'], #blue
                          (128, 140, 253): self.CHORDS['F#minor'], #dark blue
                          (145, 0, 255): self.CHORDS['Dbminor'], #purple
                          (188, 118, 252): self.CHORDS['Abminor'], #light purple
                          (142, 51, 107): self.CHORDS['Ebminor'], #pink
                          (171, 103, 125): self.CHORDS['Bbminor'], #skin color
                          (173, 0, 49): self.CHORDS['Fminor'] # velvet
                         }
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
    
    @staticmethod
    def get_bpm(entropy, max_entropy, min_entropy):
        max_bpm = Color2Music.MAX_BPM
        min_bpm = Color2Music.MIN_BPM

        bpm = convert_range(max_entropy, min_entropy, max_bpm, min_bpm, entropy)
        return bpm
    
    @staticmethod
    def get_octave(luminance, max_lum, min_lum):
        max_oct = Color2Music.MAX_OCTAVE
        min_oct = Color2Music.MIN_OCTAVE

        octave = convert_range(max_lum, min_lum, max_oct, min_oct, luminance)
        return octave