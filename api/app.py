from flask import Flask, jsonify
from flask_cors import CORS
from extract_color import ExtractColor
from process_image import SplitImage
from color_to_music import Color2Music
import time
import os
import numpy as np
from flask_caching import Cache

# parameters
DATA_DIR = "../src/assets"
CACHE_DIR = "cache"
cache_config = {
    "DEBUG": True,    
    "CACHE_TYPE": "FileSystemCache",
    "CACHE_DEFAULT_TIMEOUT": 0,
    "CACHE_DIR": CACHE_DIR
}
NUM_SECTIONS = 8

# set up flask app
app = Flask(__name__)
app.config.from_mapping(cache_config)
CORS(app)
cache = Cache(app)

@app.route("/")
def api():
    return "interactive-art api", 200

@app.route('/coords/<image>/<int:width>/<int:height>/')
def get_notes(image, width, height):
    start = time.time()

    # get primary color from each section of the image
    # it will be cached if a given image has been seen before with the same number of sections
    colors = extract_colors(image, NUM_SECTIONS)

    # convert color to music note for each chunk and create a coordinate map with all notes
    i = 0
    note_coord = np.ones((width, height), dtype=object) * -1
    split = SplitImage((width, height), NUM_SECTIONS)
    for chunk in split.get_chunks():
        color = colors[i]
        color2mus = Color2Music(color)
        note = color2mus.get_note()

        note_coord[chunk[0]:chunk[2], chunk[1]:chunk[3]] = note
        i += 1
    
    if -1 in np.unique(note_coord):
            print(note_coord)
            print("image size", width, height)
            raise Exception("Not all image area was initialized")

    end = int(time.time() - start)
    print(f"processed image in: {end} seconds")

    response = {"notes": note_coord.tolist()}
    return jsonify(response), 200

@cache.memoize()
def extract_colors(f_name, num_split):
    print("primary image colors not cached")
    
    img_path = os.path.join(DATA_DIR, f_name)
    ext_color = ExtractColor(img_path, num_split)
    return ext_color.get_color_sections()

if __name__ == '__main__':
    port_num = 5000
    app.run(host='localhost', port=port_num, debug=True)