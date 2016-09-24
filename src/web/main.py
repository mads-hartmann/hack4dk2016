from flask import Flask
from flask import render_template
from flask import request
from common import data
from mysql.connector import (connection)

from common import db

app = Flask(__name__)

cnx = connection.MySQLConnection(
    user='root',
    # password='tiger',
    host='127.0.0.1',
    database='hack4dk2016')


@app.route('/', methods=['GET'])
def index():
    return render_template(
        'pages/index.jinja.html',
        pictures=db.random_pictures(cnx, 6))


@app.route('/lastnames', methods=['GET'])
def lastnames():
    lastnames = db.all_last_names(cnx)
    return render_template(
        'pages/lastnames.jinja.html',
        lastnames=lastnames)


@app.route('/firstnames', methods=['GET'])
def firstnames():
    firstnames = db.all_first_names(cnx)
    return render_template(
        'pages/firstnames.jinja.html',
        firstnames=firstnames)


@app.route('/lastnames/<last_name>', methods=['GET'])
def last_name(last_name):
    people = list(db.with_last_name(cnx, last_name))
    return render_template(
        'pages/lastname.jinja.html',
        last_name=last_name,
        people=people)


@app.route('/firstnames/<first_name>', methods=['GET'])
def first_name(first_name):
    people = list(db.with_first_name(cnx, last_name))
    return render_template(
        'pages/firstname.jinja.html',
        first_name=first_name,
        people=people)


@app.route('/picture/<picture_id>', methods=['GET'])
def picture_page(picture_id):
    people = list(db.with_picture_id(cnx, picture_id))
    image_url = people[0].image_url
    return render_template(
        'pages/picture.jinja.html',
        picture_id=picture_id,
        image_url=image_url,
        people=people)


if __name__ == '__main__':
    app.debug = True
    app.static_folder = '../../static'
    app.run('0.0.0.0', port=8080)
