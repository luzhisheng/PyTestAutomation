import json
import os


current_directory = os.getcwd()  # 获取当前工作目录
parent_directory = os.path.dirname(current_directory)  # 获取上一级目录


def read_json(key, file_name=None):
    if file_name:
        file_path = parent_directory + file_name
    else:
        file_path = parent_directory + r"\Config\user_data.json"
    with open(file_path, encoding='utf-8') as f:
        data = json.load(f)
    return data.get(key)
