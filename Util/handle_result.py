from deepdiff import DeepDiff


def handle_result(dict_1, dict_2):
    """
    校验字典结果字段
    :return:
    """
    if isinstance(dict_1, dict) and isinstance(dict_2, dict):
        cmp_dict = DeepDiff(dict_1, dict_2, ignore_order=True).to_dict()
        if cmp_dict.get("dictionary_item_added"):
            return False
        else:
            return True
    else:
        return False


if __name__ == '__main__':
    dict1 = {"aaa": "AAA", "bb1": "BBB", "cc": [{"11": "22"}, {"11": "22"}]}
    dict2 = {"aaa": "111", "bbb": "BBB", "cc": [{"11": "223333"}, {"11": "22"}]}
    handle_result(dict1, dict2)
