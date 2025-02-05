def decodeString(s):
    s = []
    ds = ''
    rc = 0
    
    for char in s:
        if char.isdigit():
            rc = rc * 10 + int(char)
        elif char == '[':
            s.append((ds, rc))
            ds = ''
            rc = 0
        elif char == ']':
            prev_dc, prev_rc = s.pop()
            ds = prev_dc + ds * prev_rc
        else:
            ds += char
    return ds
s = "3[a]2[bc]"
print(decodeString(s))
