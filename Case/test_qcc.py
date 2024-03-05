from Util.handle_excel import HandExcel
from base_request import request
from Util.handle_json import read_json
import unittest
import ddt


@ddt.ddt
class TestQcc(unittest.TestCase):
    hand_excel = HandExcel('qcc.xlsx')
    data = hand_excel.load_excel().values
    base_url = "http://127.0.0.1:5555"

    def setUp(self) -> None:
        print("case开始执行")

    def tearDown(self) -> None:
        print("case执行结束")

    @ddt.data(*data)
    def test_01(self, data_1):
        case, activity, is_run, term, url, method, param_data, cookie, header, my_variable, is_pass, result = data_1

        param_data = read_json(f'{case}|{url}', r"\Config\请求参数.json")
        url = self.base_url + url

        if is_run == 'yes':
            flag, res = request.run_main(method=method, url=url, data=param_data)

            try:
                if "json格式" in my_variable:
                    # 判断json格式是否正确
                    if flag:
                        print("测试json格式通过")
                    else:
                        print("测试json格式失败")

                if "状态码" in my_variable:
                    # 判断状态码是否正确
                    self.assertEqual(res['status'], 200)

                if "字段对比" in my_variable:
                    pass

            except Exception as e:
                print(e)
            else:
                self.hand_excel.write_excel(case, '是否通过', '通过')


if __name__ == '__main__':
    unittest.main()
