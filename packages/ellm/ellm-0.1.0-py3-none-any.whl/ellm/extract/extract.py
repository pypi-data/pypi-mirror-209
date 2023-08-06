import json

from jsonpath import jsonpath


class Extractor(object):
    def __init__(self):
        pass

    def extract(self, data, path):
        if type(data) is str:
            data = json.loads(data)
        return jsonpath(data, path)
