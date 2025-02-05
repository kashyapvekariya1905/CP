def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    rows = ['']*numRows
    cr = 0
    down = False

    for i in s:
        rows[cr]+=i
        if cr == 0 or cr==numRows-1:
            down = not down
        cr += 1 if down else -1
    return ''.join(rows)
 
s = "late in the lab is not allowed"
numRows = 4

# P   A   H   N
# A P L S I I G
# Y   I   R

# s = "PAYPALISHIRING"
# numRows = 4

# P     I    N
# A   L S  I G
# Y A   H R
# P     I

print(convert(s,numRows))