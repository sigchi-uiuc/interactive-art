from flask import Flask, jsonify
from flask_cors import CORS
from process_image import ProcessImage
import time
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

# set up flask app
app = Flask(__name__)
app.config.from_mapping(cache_config)
CORS(app)
cache = Cache(app)

@app.route("/")
def api():
    return "interactive-art api", 200

@app.route('/coords/<image>/<int:width>/<int:height>/')
@cache.memoize()
def get_notes(image, width, height):
    start = time.time()

    process = ProcessImage(image, 
                          DATA_DIR, 
                          target_width=width, 
                          target_height=height)
    coords, images = process.divide_image()

    end = int(time.time() - start)
    print(f"processed image in: {end} seconds")

    response = {"notes": coords.tolist()}
    return jsonify(response), 200

if __name__ == '__main__':
    port_num = 5000
    app.run(host='localhost', port=port_num, debug=True)