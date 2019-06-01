def convert(s):
    s = s.strip('&#x;')
    s = bytes(r'\u' + s, 'gb2312')
    return s.decode('unicode_escape')

def str_decode(s):
    print(s.decode('utf8'))
    print(s.decode('gb2312'))
print(convert('&#xEE3A;'))

'''
&#xEE3A;.&#xEE3A;&#xE8BC;
'''