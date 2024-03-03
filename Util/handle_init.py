import configparser
import os

current_directory = os.getcwd()  # 获取当前工作目录
parent_directory = os.path.dirname(current_directory)  # 获取上一级目录


class HandleInit(object):

    def load_ini(self):
        cf = configparser.ConfigParser()
        cf.read(parent_directory + r"\Config\server.ini", encoding="utf-8-sig")
        return cf

    def get_value(self, key):
        """
        获取ini里面的 value
        :return:
        """
        cf = self.load_ini()
        value = cf.get('server', key)
        return value


handle_init = HandleInit()


if __name__ == '__main__':
    handle_init = HandleInit()
    res = handle_init.get_value('username')
    print(res)
