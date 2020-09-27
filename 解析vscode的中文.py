#!/usr/bin/env python
#解析vscode的乱码字符
#瀵规瘮鏃犳煡璇㈡椂鐨勫唴瀛樹娇鐢ㄧ姸鎬?
#对比无查询时的内存使用状态
import pyperclip
print('对比无查询时的内存使用状态'.encode('utf-8'))

print('瀵规瘮鏃犳煡璇㈡椂鐨勫唴瀛樹娇鐢ㄧ姸鎬？'.encode('gbk').decode('utf-8',"ignore"))
