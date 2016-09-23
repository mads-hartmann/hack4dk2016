# -*- coding: utf-8 -*-

import json

def load_from_json():
    with open('data/identified-people.json') as json_data:
        json_object = json.load(json_data)
        return list(parse(json_object))

def parse(json_object):
    objects = json_object['data']
    for obj in objects:
        yield Picture.from_json(obj)


class Picture(object):
    def __init__(self, first_name, last_name, mothers_name, fathers_name, picture_id):
        self.first_name = first_name
        self.last_name = last_name
        self.mothers_name = mothers_name
        self.fathers_name = fathers_name
        self.picture_id = picture_id

    @classmethod
    def from_json(cls, obj):
        first_name = obj['Fornavn']
        last_name = obj['Efternavn']
        fathers_name = obj['Faders navn']
        mothers_name = obj['Moders navn']
        picture_id = obj['Billednummer']
        return Picture(
            first_name, last_name,
            mothers_name, fathers_name,
            picture_id)

    # def __str__(self):
    #     return u'Picture({},{},{},{},{})'.format(
    #         self.first_name,
    #         self.last_name,
    #         self.mothers_name.encode('utf-8'),
    #         self.fathers_name,
    #         self.picture_id)

    # def __repr__(self):
    #     return str(self).encode('utf-8')
