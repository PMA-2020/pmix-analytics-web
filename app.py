"""App"""
import platform
import os

from flask import Flask

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
path_char = '\\' if platform.system() == 'Windows' else '/'


@app.route('/', methods=['GET', 'POST'])
def index():
    """Index"""
    return 'hello world'


if __name__ == '__main__':
    app.run(debug=True)
