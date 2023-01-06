import math

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