import time
import os
import traceback
from typing import Literal


# 獲取當前時間
def get_time(_type="%Y-%m-%d %H:%M:%S"):
    return time.strftime(_type, time.localtime(time.time()))

# log紀錄標準格式
def log_writing_type(file, _type, _time, text) -> str:
    return f'[{file}]-[{_type}] ({_time})>> {text}\n'

class TestLog:
    """自製Log紀錄檔
       ~~~~~~~~~~~
    """
    def __init__(self, file_name, path = get_time("%Y-%m-%d_%H-%M-%S")) -> None:
        self.log_path = f'./log/log_{path}.txt'
        self.log_file_name = file_name
        self.before = ''
        self.build_file()
    
    def build_file(self):
        self.build_logdir()
        build_time = get_time()
        with open(file=self.log_path, mode='a', encoding='utf-8') as files:
            files.write(self.before)
            files.write(log_writing_type('Log.py', 'info', build_time, 'build log.'))
    
    def build_logdir(self):
        if not os.path.isdir('./log'):
            os.mkdir('./log')
            self.before = log_writing_type('Log.py', 'info', get_time(), 'build log dir.')
    
    # 標準log輸入
    def add_str(self, _str: str, _type: Literal['info', 'event', 'warning']):
        with open(file=self.log_path, mode='a', encoding='utf-8') as files:
            now_time = get_time()
            files.write(log_writing_type(self.log_file_name, _type, now_time, _str))
    
    # 可自定義檔案名稱的輸入
    def add_pkg_str(self, file_name: str, _str: str, _type: Literal['info', 'event', 'warning']):
        with open(file=self.log_path, mode='a', encoding='utf-8') as files:
            now_time = get_time()
            files.write(log_writing_type(file_name, _type, now_time, _str))
    
    # 根據try捕獲報錯內容紀錄
    def write_error(self, error: Exception, _type: Literal['info', 'event', 'warning'] = 'warning'):
        tb = error.__traceback__
        stack_info = traceback.extract_tb(tb)
        for i in stack_info:
            self.add_pkg_str(os.path.basename(i.filename), f'line: {i.lineno}, func: {i.name}, msg: {str(error)}', _type)
            

if __name__ == '__main__':
    l = TestLog('test..')
    l.add_str('test', 'info')