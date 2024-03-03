from Util.handle_json import read_json


def handle_result(url, code):
    list_data = read_json(url, r"\Config\code_message.json")
    if list_data:
        for i in list_data:
            message = i.get(str(code))
            if message:
                return message
    return None


if __name__ == '__main__':
    a = handle_result('api3/getbanneradverver', '10002')
    print(a)
