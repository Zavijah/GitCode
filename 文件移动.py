# 本程序用于将子文件夹下的文件移动到当前文件夹

import os
import shutil
from pprint import pprint

file_list = os.listdir('./old/')
for d in file_list:
    files = os.listdir(f'./old/{d}/')
    for f in files:
        if 'mp4' in f:
            shutil.copyfile(f'./old/{d}/{f}', f'./new/{f}')
