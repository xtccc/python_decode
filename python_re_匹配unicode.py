#!/usr/bin/env python
import pyperclip
import re
import time
print('脚本开始运行')
while True:
    tmp_value = pyperclip.paste()   # 读取剪切板复制的内容
    pattern = r'\\u[a-z,A-Z,0-9][a-z,A-Z,0-9][a-z,A-Z,0-9][a-z,A-Z,0-9]'
    string = tmp_value
    changed = tmp_value
    if re.search(pattern, string):
        restlut = re.finditer(pattern, string)
        # print(restlut)
        for i in restlut:
            # print(i)
            # print(i.span())
            # print(i.group())
            raw = str(i.group())
            i_chi = raw.encode('utf-8').decode('unicode_escape')
            # print(i_chi)
            changed = changed.replace(raw, i_chi)
            # print(changed)

        #result_index = restlut.span()[0]
        # tmp_value =
    pyperclip.copy(changed)  # 将修改后的文本写入系统剪切板中
    time.sleep(0.5)
# sssssss\u672a\u627e\u5230\u547d\u4ee4ssssss\u672a\u627essss\u672a\u627essss\u672a\u627essss\u672a\u627e
#re.search(pattern, string)