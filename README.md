# unicode字符转为中文

用于linux使用vnc复制vncviewer的文字出现unicode符号时，使用本脚本将剪切版中的uncodede符号转为中文

# 安装

git clone git@github.com:xtccc/python_decode.git

pip install  pyperclip

sudo chmod +x python_re_匹配unicode.py

# 使用

./python_re_匹配unicode.py


# 带解决的vnc内vscode思路
用is_rare_name函数解决乱码的判断，加以gbk的解码即可