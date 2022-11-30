from flask import Flask, jsonify
from flask_cors import CORS
from process_image import ProcessImage
import time

app = Flask(__name__)
CORS(app)
data_dir = "../ui/interactive-art-VUE/src/assets"

@app.route('/api/coords/<image>/<int:width>/<int:height>/', methods=['GET'])
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
    port_num=4000
    app.run(host='localhost', port=port_num, debug=True)