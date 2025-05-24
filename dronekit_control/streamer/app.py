# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template, url_for
import random
import os

app = Flask(__name__, static_folder='static', template_folder='templates')


# Main page (Loads once)
@app.route('/')
def index():
    return render_template('index.html')

# API for updating images & sensor data (Called via JavaScript)
@app.route('/update_data')
def update_data():
    #data = get_sensor_data()
    return jsonify({
        "image1": url_for('static', filename='output.jpg') + "?v=" + str(random.randint(1, 10000)),  
    })

if __name__ == '__main__':
    if not os.path.exists('static'):
        os.makedirs('static')
    
    app.run(host='0.0.0.0', port=5000, debug=True)
