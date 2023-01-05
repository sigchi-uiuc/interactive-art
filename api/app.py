from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from process_image import ProcessImage
import time

data_dir = "../src/assets"

app = Flask(__name__)
CORS(app)

@app.route("/")
def api():
    return "interactive-art api", 200

@app.route('/coords/<image>/<int:width>/<int:height>/')
def get_notes(image, width, height):
    start = time.time()

    process = ProcessImage(image, 
                          data_dir, 
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