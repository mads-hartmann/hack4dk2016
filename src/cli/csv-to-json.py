#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import json
import argparse
import io


def convert(input_file, output_file):
    csvfile = open(input_file, 'r')
    jsonfile = open(output_file, 'w')

    fieldnames = (
        "Billednummer",
        "Fornavn",
        "Efternavn",
        "Titel",
        "Født",
        "Død",
        "Billedets datering",
        "Adresse på tidspunktet for fotoet",
        "Faders navn",
        "Moders navn",
        "Gift med",
        "Børn",
        "Bemærkninger",
        "Fødested",
        "Dødssted",
        "Vielsessted",
        "Vielsesdato",
        "Fødenavn",
        "Gift med 2. gang",
        "Vielsesdato 2. gang",
        "Vielsessted 2. gang")

    reader = csv.DictReader(csvfile, fieldnames)

    jsonfile.write('{ "data": [\n')
    for row in list(reader)[1:-1]:
        cleaned_obj = {
            k: v.replace('"','').strip().replace('\n','')
            for k,v in row.iteritems()
            if k is not None
        }
        jsonfile.write(json.dumps(cleaned_obj).decode('unicode-escape').encode('utf8'))
        jsonfile.write(',\n')

    jsonfile.write('}]\n')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='CSV file to read from', type=str)
    parser.add_argument('--output', help='JSON file to write to', type=str)
    args = parser.parse_args()
    convert(args.input, args.output)

