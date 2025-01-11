import numpy as np
from flask import Flask, request, jsonify, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import subprocess


# Create flask app
flask_app = Flask(__name__)


@flask_app.route("/")
def Home():
    result = subprocess.run(['python', 'main7.py'], capture_output=True)
    return result.stdout.decode('utf-8')



if __name__ == "__main__":
    flask_app.run(debug=True)