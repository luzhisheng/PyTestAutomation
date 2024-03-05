from setting import current_directory
import pandas as pd


class HandExcel(object):

    def __init__(self, xlsx_name):
        self.xlsx_name = xlsx_name

    def load_excel(self, sheet_name=0):
        """
        加载excel
        :return:
        """
        df = pd.read_excel(current_directory + fr'\File\{self.xlsx_name}', sheet_name)
        return df

    def get_cell_value(self, row, cols_name):
        """
        获取某个单元格内容
        :return:
        """
        df = self.load_excel()
        data_label = df.at[row, cols_name]
        return data_label

    def get_rows(self):
        """
        获取行数
        :return:
        """
        df = self.load_excel()
        num_rows = len(df)
        return num_rows

    def get_rows_value(self, row=0):
        """
        获取某一行的内容
        :return:
        """
        df = self.load_excel()
        row_by_label = df.loc[row].tolist()
        return row_by_label

    def write_excel(self, row_value, cols, value):
        """
        写入某个单元格数据
        :return:
        """
        df = self.load_excel()
        df.loc[df['case编号'] == row_value, cols] = value
        df.to_excel(current_directory + fr'\File\{self.xlsx_name}', index=False)
        return df


if __name__ == '__main__':
    hand_excel = HandExcel('qcc.xlsx')
    hand_excel.write_excel(0, '测试执行结果', '通过')
    hand_excel.write_excel(1, '测试执行结果', '通过')
