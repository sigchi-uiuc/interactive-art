from flask import Flask, jsonify, send_file, render_template, request

app = Flask(__name__)

@app.route('/api')
def index():
    return render_template('index.html')