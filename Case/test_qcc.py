from Util.handle_excel import HandExcel
from Case.base import Base
from base_request import request
from Util.handle_json import read_json
from Util.handle_result import handle_result
import unittest
import ddt


@ddt.ddt
class TestQcc(unittest.TestCase, Base):
    hand_excel = HandExcel('qcc.xlsx')
    data = hand_excel.load_excel().values
    base_url = "http://127.0.0.1:5555"

    def setUp(self) -> None:
        self.log("case开始执行")

    def tearDown(self) -> None:
        self.log("case执行结束")

    @ddt.data(*data)
    def test_01(self, data_1):
        case, activity, is_run, term, url, method, param_data, cookie, header, my_variable, is_pass = data_1

        param_data = read_json(f'{case}|{url}', r"\Config\请求参数.json")
        res_data = read_json(f'{case}|{url}', r"\Config\预期结果.json")

        url = self.base_url + url

        if is_run == 'yes':
            flag, res = request.run_main(method=method, url=url, data=param_data)

            try:
                try:
                    if "json格式" in my_variable:
                        # 判断json格式是否正确
                        self.assertTrue(flag)
                        self.log("测试json格式通过")
                except Exception as e:
                    self.log("测试json格式失败")
                    raise e

                try:
                    if "状态码" in my_variable:
                        # 测试状态码是否正确
                        self.assertEqual(res['status'], 200)
                        self.assertEqual(res['message'], "成功")
                        self.log("测试状态码通过")
                except Exception as e:
                    self.log("测试状态码失败")
                    raise e

                try:
                    if "字段对比" in my_variable:
                        flag_field = handle_result(res, res_data)
                        self.assertTrue(flag_field)
                        self.log("测试字段对比通过")
                except Exception as e:
                    self.log("测试字段对比失败")
                    raise e

            except Exception as e:
                raise e
            else:
                self.hand_excel.write_excel(case, '是否通过', '通过')


if __name__ == '__main__':
    unittest.main()
