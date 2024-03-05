import unittest
from setting import current_directory
import HTMLTestRunner
from Case.test_qcc import TestQcc

suite = unittest.TestLoader().loadTestsFromTestCase(TestQcc)
file_path = current_directory + r"\Report\report.html"
with open(file_path, 'wb') as f:
    # 创建 HTMLTestRunner 实例
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=f,
        title='测试报告',
        description='测试用例结果'
    )
    # 运行测试套件
    runner.run(suite)
