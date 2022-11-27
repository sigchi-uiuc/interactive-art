from flask import Flask, jsonify, request
from process_image import ProcessImage
import json
import os

app = Flask(__name__)

@app.route('/api/coords/<image>/<int:width>/<int:height>', methods=['GET'])
def get_notes(image, width, height):
    print(image)
    print(width, height)
    data_dir = "../ui/interactive-art-VUE/src/assets"
    process = ProcessImage(image, data_dir)
    coords, images = process.divide_image(8)

    j = json.dumps(coords.tolist())
    return jsonify(j), 200

if __name__ == '__main__':
    port_num=4000
    app.run(host='0.0.0.0', port=port_num)