from deepdiff import DeepDiff


def handle_result(dict1, dict2):
    """
    校验结果字段
    :return:
    """
    if isinstance(dict1, dict) and isinstance(dict2, dict):
        cmp_dict = DeepDiff(dict1, dict2, ignore_order=True).to_dict()
        if cmp_dict.get("dictionary_item_added"):
            print("case失败")
            return False
        else:
            print("case成功")
            return True
    else:
        return False


if __name__ == '__main__':
    dict1 = {"aaa": "AAA", "bb1": "BBB", "cc": [{"11": "22"}, {"11": "22"}]}
    dict2 = {"aaa": "111", "bbb": "BBB", "cc": [{"11": "223333"}, {"11": "22"}]}
    handle_result(dict1, dict2)
