from flask import Flask
from flask import render_template
from flask import request
from common import data


app = Flask(__name__)
app.pictures = data.load_from_json()


@app.route('/', methods=['GET'])
def index():
    return render_template(
        'index.jinja.html', pictures=app.pictures[0:10])


@app.route('/<picture_id>', methods=['GET'])
def picture_page(picture_id):
    picture = [p for p in app.pictures if p.picture_id == picture_id][0]
    return render_template(
        'picture.jinja.html',
        first_name=picture.first_name,
        picture_id=str(picture.picture_id).zfill(4))


if __name__ == '__main__':
    app.debug = True
    app.static_folder = '../../static'
    app.run('0.0.0.0', port=8080)
