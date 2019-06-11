import yaml
from flask import Flask
from flask import request
from flask import send_from_directory

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return send_from_directory('public', 'index.html')


@app.route('/convert', methods=['POST'])
def convert():
    converted_yml = yaml.dump(yaml.load(request.get_data().decode("utf-8")))
    return converted_yml


@app.route('/<path:path>', methods=['GET'])
def static_folder(path):
    return send_from_directory('public', path)


if __name__ == '__main__':
    app.run()
