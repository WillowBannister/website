from google.cloud import datastore
import random
import json

paint_col = ['id_paint','product','image']

def google_get(entity, col):
    client = datastore.Client()
    result = client.query(kind=entity).fetch()
    print(type(result))
    output = []
    for entity in result:
        test = {}
        for y in col:
            test[y] = entity[y]
        output.append(test)

    return output