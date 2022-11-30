from flask import Flask, jsonify, request
from flask_cors import CORS
from process_image import ProcessImage
import json
import os

app = Flask(__name__)
CORS(app)
data_dir = "../ui/interactive-art-VUE/src/assets"

@app.route('/api/coords/<image>/<int:width>/<int:height>/', methods=['GET'])
def get_notes(image, width, height):
    process = ProcessImage(image, 
                          data_dir, 
                          target_width=width, 
                          target_height=height)
    
    coords, images = process.divide_image()

    response = {"notes": coords.tolist()}
    # response = json.dumps(coords.tolist())
    return response, 200

if __name__ == '__main__':
    port_num=4000
    app.run(host='localhost', port=port_num, debug=True)