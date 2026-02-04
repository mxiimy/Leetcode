def getKeyIdentifier(key: str)->str:
    if len(key)<=1:
        return key
    chars = []
    for char in key:
        chars.append(char)
    chars.sort()
    s = []
    e = []
    mid = []
    while len(chars)>1: 
        if chars[0] == chars[1]:
            s.append(chars[0])
            e.append(chars[1])
            chars = chars[2:]
        else:
            mid.append(chars[0])
            chars = chars[1:]
    midi = len(s) //2
    e.reverse()
    
    if len(chars) > 0:
        joined = s + chars + e
        return ''.join(joined)
    elif len(mid) > 0:
        joined = s + mid + e
        return ''.join(joined)
    else:
        joined = s + e
        return ''.join(joined)