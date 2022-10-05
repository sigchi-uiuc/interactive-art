from PIL import Image
import math
import numpy as np

class ProcessImage:
    def __init__(self, f_name):
        self.image = Image.open(f_name)
        self.size = self.image.size
        self.x, self.y = self.size

    def divide_image(self, num_sections=4):
        cols, rows = self._get_num_rows_cols(num_sections)
        width = int(math.ceil(self.x / cols))
        height = int(math.ceil(self.y / rows))

        coord_map = np.ones(self.size, dtype=int) * -1
        images = []
        for x in range(0, self.x - cols, width):
            for y in range(0, self.y - rows, height):
                # crop image
                area = (x, y, x+width, y+height)
                image_section = self.image.crop(area)

                # map image location to section
                images.append(image_section)
                i = len(images) - 1
                coord_map[x:x+width, y:y+height] = i

        if -1 in np.unique(coord_map):
            print(coord_map)
            print("image size", self.size)
            print("num cols", cols, "num rows", rows)
            print("section width", width, "section height", height)
            raise Exception("Not all image area was initialized")

        return coord_map, images
    
    def _get_num_rows_cols(self, num_sections):
        cols = int(math.ceil(math.sqrt(num_sections)))
        rows = int(math.ceil(num_sections / float(cols)))
        return (cols, rows)
