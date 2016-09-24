from flask import Flask
from flask import render_template
from flask import request
from common import data


app = Flask(__name__)
app.pictures = data.load_from_json()


@app.route('/', methods=['GET'])
def colors_page():
    return render_template(
        'index.jinja.html', pictures=app.pictures[0:10])


if __name__ == '__main__':
    app.debug = True
    app.static_folder = '../../static'
    app.run('0.0.0.0', port=8080)
