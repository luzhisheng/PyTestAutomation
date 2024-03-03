from Util.handle_excel import HandExcel
from base_request import request
from Util.handle_result import handle_result


class TestQcc(object):

    def run_case(self):
        hand_excel = HandExcel('qcc.xlsx')
        rows = hand_excel.get_rows()
        for i in range(rows):
            row_by_label = hand_excel.get_rows_value(i)
            print(row_by_label)
            is_run = row_by_label[2]
            if is_run == 'yes':
                method = row_by_label[5]
                url = row_by_label[4]
                data = row_by_label[6]
                res = request.run_main(method=method, url=url, data=data)
                code = res.get('errorCode')
                message = res.get('errorDesc')
                config_message = handle_result(url=url, code=code)
                if message == config_message:
                    print("测试case通过")
                else:
                    print("测试case失败")


if __name__ == '__main__':
    run_main = TestQcc()
    run_main.run_case()
