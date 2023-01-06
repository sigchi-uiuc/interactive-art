from PIL import Image
import math
import numpy as np
from extract_color import ExtractColor
from color_to_music import Color2Music
import os

class ProcessImage:
    def __init__(self, f_name, data_dir, target_width=None, target_height=None):
        self.data_dir = data_dir
        self.image = Image.open(os.path.join(data_dir, f_name))

        print("original image size", self.image.size)

        # resize image to requested screen size
        if not ((target_width is None) or (target_height is None)):
            self.image = self.image.resize((target_width, target_height))

        self.size = self.image.size
        self.x, self.y = self.size

        print("new image size", self.size)

    def divide_image(self, num_sections=8):
        print(f"splitting into {num_sections}")

        split = SplitImage(self.size, num_sections)
        chunk_gen = split.get_chunks()

        note_coord = np.ones(self.size, dtype=object) * -1
        images = []
        for chunk in chunk_gen:
            image_section = self.image.crop(chunk)
            images.append(image_section)
            i = len(images) - 1

             # get dominant color
            extract = ExtractColor(image_section)
            dominant_color = extract.get_dominant()

            # get music note from dominant color
            music = Color2Music(dominant_color)
            note = music.get_note()

            print(f'section: {i}, dominant color: {dominant_color}, note: {note}')

            # map image location to note
            note_coord[chunk[0]:chunk[2], chunk[1]:chunk[3]] = note

        if -1 in np.unique(note_coord):
            print(note_coord)
            print("image size", self.size)
            raise Exception("Not all image area was initialized")

        return note_coord, images

class SplitImage:
    def __init__(self, img_size, num_sections):
        self.img_width = img_size[0]
        self.img_height = img_size[1]

        self.cols, self.rows = self._get_num_rows_cols(num_sections)

        self.width = int(math.ceil(self.img_width / self.cols))
        self.height = int(math.ceil(self.img_height / self.rows))

    # iterates over split image in row then column order
    def get_chunks(self):
        for x in range(0, self.img_width - self.cols, self.width):
            for y in range(0, self.img_height - self.rows, self.height):
                area = (x, y, x+self.width, y+self.height)
                yield area
    
    def _get_num_rows_cols(self, num_sections):
        cols = int(math.ceil(math.sqrt(num_sections)))
        rows = int(math.ceil(num_sections / float(cols)))
        return (cols, rows)