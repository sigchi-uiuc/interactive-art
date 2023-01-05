from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from process_image import ProcessImage
import time
import dotenv
import os

dotenv.load_dotenv()

SUBDOMAIN = os.getenv("SUBDOMAIN")
data_dir = "../src/assets"

app = Flask(__name__)
CORS(app)

@app.route("/", subdomain=SUBDOMAIN)
def api():
    return "interactive-art api", 200

@app.route('/coords/<image>/<int:width>/<int:height>/', subdomain=SUBDOMAIN)
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
    if SUBDOMAIN:
        app.config['SERVER_NAME']='localhost:5000'

    app.run()