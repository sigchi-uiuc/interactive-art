from flask import Flask, jsonify
from flask_cors import CORS
from process_image import SplitImage, get_notes_colors
import time
import os
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
    colors, notes = extract_notes_colors(image, NUM_SECTIONS)

    # scale notes and colors to new area based on split image
    i = 0
    response = []
    split = SplitImage((width, height), NUM_SECTIONS)
    for chunk in split.get_chunks():
        color = colors[i]
        note = notes[i]

        data = {}
        data['color'] = color
        data['note'] = note
        data['area'] = chunk

        response.append(data)
        i += 1

    end = int(time.time() - start)
    print(f"processed image in: {end} seconds")

    return jsonify(response), 200

@cache.memoize()
def extract_notes_colors(f_name, num_split):
    print("primary image colors not cached")
    
    img_path = os.path.join(DATA_DIR, f_name)
    return get_notes_colors(img_path, num_split)

if __name__ == '__main__':
    port_num = 5000
    app.run(host='localhost', port=port_num, debug=True)