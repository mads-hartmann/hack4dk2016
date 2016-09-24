# -*- coding: utf-8 -*-
import json

with open('data/identified-people.json') as json_data:
    d = json.load(json_data)
    #print(d)


for ii in range(0,len(d['data'])):
    fullNameMother = d['data'][ii]['Moders navn']
    fullNameFather = d['data'][ii]['Faders navn']
    #print(d['data'][ii]['Born'])
    #for jj in range(0,len(d['data'])):
    #    fullNameMother2 = d['data'][jj]['Moders navn']
    #    if fullNameMother==fullNameMother2:
    #        print(fullNameMother)
    #        print(d['data'][ii]['Fornavn']+ ' ' +d['data'][ii]['Efternavn'])
    #        print(d['data'][jj]['Fornavn']+ ' ' +d['data'][jj]['Efternavn'])

    #    if (len(fullNameMother)>0)&(fullNameMother==fullNameChild):
            #print(fullNameMother)
    #        childCount = childCount + 1;
        #if (len(fullNameFather)>0)&(fullNameFather==fullNameChild):
    #if childCount>0:
    #    print(fullNameMother)
    #    print(childCount)
