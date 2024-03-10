import json


def load_schema(schema):
    with open(schema) as file:
        return json.loads(file.read())
