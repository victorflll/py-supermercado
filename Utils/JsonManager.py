import json
import os


def create_json(file_path: str, data=None):
    if data is None:
        data = []
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2, separators=(',', ': '))
        file.close()
        return data


def open_json(file_path: str, data=None):
    if data is None:
        data = []
    path = os.getcwd() + file_path

    exists = os.path.isfile(path)

    if exists:
        with open(path) as file:
            data = json.load(file)
            file.close()
            return data
    else:
        return create_json(path, data)


def update_json(file_path: str, data):
    path = os.getcwd() + file_path

    exists = os.path.isfile(path)

    if exists:
        with open(path, 'w') as file:
            json.dump(data, file, indent=2, separators=(',', ': '))
            file.close()
    else:
        create_json(path)


class JsonManager:
    pass
