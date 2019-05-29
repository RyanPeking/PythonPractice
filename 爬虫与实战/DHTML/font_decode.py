def convert(s):
    s = s.strip('&#x;')
    s = bytes(r'\u' + s, 'ascii')
    return s.decode('unicode_escape')

print(convert('&#xEE3A;'))

'''
&#xEE3A;.&#xEE3A;&#xE8BC;
'''