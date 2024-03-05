from setting import current_directory
import json
import os


def read_json(key, file_name=None):
    if file_name:
        file_path = current_directory + file_name
    else:
        file_path = current_directory + r"\Config\user_data.json"
    with open(file_path, encoding='utf-8') as f:
        data = json.load(f)
    return data.get('app').get(key)
