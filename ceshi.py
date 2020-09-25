#!/home/xtcc/anaconda3/bin/python3.8 
import pyperclip
changed  = pyperclip.paste() 			# 读取剪切板复制的内容
print("已读取:",changed)
changed = changed.encode('utf-8').decode('unicode_escape')
print("已读取:",changed)
pyperclip.copy(changed) 				#将修改后的文本写入系统剪切板中



str = '\u8fd0'
print(str)