import csv
import re
import traceback
import argparse
from datetime import datetime

from mysql.connector import (connection)

cnx = connection.MySQLConnection(
    user='root',
    # password='tiger',
    host='127.0.0.1',
    database='hack4dk2016')


def parse_date(s):
    if not s:
        return None
    try:
        return datetime.strptime(s, '%d/%m/%Y')
    except Exception as e:
        print "failed to parse {}".format(s)
        # traceback.print_exc(e)
        return None


def clean_int(s):
    return int(re.sub(r'[^\d]', '', s))


def parse_picture_date(s):
    try:
        if not s:
            return None, None

        interval = s.split('-')
        if len(interval) == 1:
            interval = (s, s)
        return clean_int(interval[0]), clean_int(interval[1])
    except Exception as e:
        print s
        traceback.print_exc(e)
        return None, None


def insert_row(obj):
    cursor = cnx.cursor()

    picture_date_start, picture_date_end = parse_picture_date(obj['picture_date'])

    cursor.execute("""
        INSERT INTO person (
            `first_name`,
            `last_name`,
            `picture_id`,
            `birthdate`,
            `death`,
            `picture_interval_year_start`,
            `picture_interval_year_end`,
            `adress_at_time_of_picture`,
            `fathers_name`,
            `mothers_name`,
            `married_with`,
            `kids`,
            `notes`,
            `place_of_birth`,
            `place_of_death`,
            `date_of_mariage`,
            `name_after_birth`,
            `2nd_mariage_partner`,
            `2nd_mariage_date`,
            `2nd_mariage_place`
        )
        VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
        );
    """, (
            obj['first_name'],
            obj['last_name'],
            obj['picture_id'],
            parse_date(obj['birthdate']),
            parse_date(obj['death']),
            picture_date_start,
            picture_date_end,
            obj['adress_at_time_of_picture'],
            obj['fathers_name'],
            obj['mothers_name'],
            obj['married_with'],
            obj['kids'],
            obj['notes'],
            obj['place_of_birth'],
            obj['place_of_death'],
            parse_date(obj['date_of_mariage']),
            obj['name_after_birth'],
            obj['2nd_mariage_partner'],
            parse_date(obj['2nd_mariage_date']),
            obj['2nd_mariage_place']
    ))
    cursor.close()


def clean(obj):
    return {
        k: v.replace('"','').strip().replace('\n','')
        for k, v in obj.iteritems()
        if k is not None
    }


def insert_into_db(csv_file):
    csvfile = open(csv_file, 'r')

    fieldnames = (
        "date",
        "picture_id",
        "first_name",
        "last_name",
        "title",
        "birthdate",
        "death",
        "picture_date",
        "adress_at_time_of_picture",
        "fathers_name",
        "mothers_name",
        "married_with",
        "kids",
        "notes",
        "place_of_birth",
        "place_of_death",
        "place_of_mariage",
        "date_of_mariage",
        "name_after_birth",
        "2nd_mariage_partner",
        "2nd_mariage_date",
        "2nd_mariage_place")

    reader = csv.DictReader(csvfile, fieldnames)

    for row in list(reader)[1:-1]:
        insert_row(clean(row))

    cnx.commit()
    cnx.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='CSV file to read from', type=str)
    args = parser.parse_args()
    insert_into_db(args.input)
