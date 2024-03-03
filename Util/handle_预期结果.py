from Util.handle_json import read_json


def handle_预期结果(key):
    list_data = read_json(key, r"\Config\预期结果.json")
    if list_data:
        return list_data
    return None


if __name__ == '__main__':
    a = handle_预期结果('api/user_list')
    print(a)
