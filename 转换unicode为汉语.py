#!/home/xtcc/anaconda3/bin/python3.8 
import time
import sys
import os
import re
sys.path.append(os.path.abspath("SO_site-packages"))
import pyperclip  # 引入模块

recent_value = ""
tmp_value="" # 初始化（应该也可以没有这一行，感觉意义不大。但是对recent_value的初始化是必须的）
changed='\0000000'
while True:
    if pyperclip.paste() == changed : 
        pass
    else:
        tmp_value = pyperclip.paste().encode('utf-8').decode('unicode_escape') 			# 读取剪切板复制的内容
    
    try:
        if tmp_value != recent_value:				 #如果检测到剪切板内容有改动，那么就进入文本的修改
            recent_value = tmp_value
            changed = out = recent_value	#将文本的换行符去掉，变成一个空格
            pyperclip.copy(changed) 							#将修改后的文本写入系统剪切板中
            print("\n Value changed: %s" % str(changed))  	# 输出已经去除换行符的文本
        time.sleep(0.5)
    except KeyboardInterrupt:  # 如果有ctrl+c，那么就退出这个程序。  （不过好像并没有用。无伤大雅）
        break
        
    if tmp_value == 'getend': # 如果复制的是getend，就退出程序。（这个主要是为了方便我在spyder中运行、退出的时候用的。）
        break
# \u672a\u627e\u5230\u547d\u4ee4