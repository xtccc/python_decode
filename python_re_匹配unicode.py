#!/usr/bin/env python
import pyperclip
import re
import time
print('脚本开始运行: 复制间隔需大于0.5')
while True:
    tmp_value = pyperclip.paste()   # 读取剪切板复制的内容
    pattern = r'\\u[a-z,A-Z,0-9][a-z,A-Z,0-9][a-z,A-Z,0-9][a-z,A-Z,0-9]'
    string = tmp_value
    changed = tmp_value
    if re.search(pattern, string):
        restlut = re.finditer(pattern, string)
        for i in restlut:
            raw = str(i.group())
            i_chi = raw.encode('utf-8').decode('unicode_escape')
            changed = changed.replace(raw, i_chi)
    pyperclip.copy(changed)  # 将修改后的文本写入系统剪切板中
    time.sleep(0.5)
# sssssss\u672a\u627e\u5230\u547d\u4ee4ssssss\u672a\u627essss\u672a\u627essss\u672a\u627essss\u672a\u627e
#re.search(pattern, string)


#\u672a\u627e\u5230\u547d\u4ee4ssssss\u672a\u627essss\u672a\u627essss\u672a\u627essss\u672a\u627e