import re

def is_rare_name(string):
    pattern = re.compile(u"[~!@#$%^&* ]")
    match = pattern.search(string)
    if match:
        return True
    try:
        string.encode("gb2312")
    except UnicodeEncodeError:
        return True
    return False

print(is_rare_name('对比无查询时的内存使用状态'))
print(is_rare_name('瀵规瘮鏃犳煡璇㈡椂鐨勫唴瀛樹娇鐢ㄧ姸鎬'))
print(is_rare_name('状态'))