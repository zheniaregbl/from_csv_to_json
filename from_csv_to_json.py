import csv
import json


def convjson(csvFilename, jsonFilename):
    data = {}

    with open(csvFilename, encoding='UTF-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for rows in reader:
            key = rows['Number']
            data[key] = rows

    with open(jsonFilename, 'w', encoding='UTF-8') as jsfile:
        jsfile.write(json.dumps(data, indent=4))


convjson('info.csv', 'info.json')
