with open('8.txt') as f:
    contents = f.read()

def is_hex_str(s):
    return all(c in '0123456789abcdef' for c in s)

res = 0

for s in contents.split("\n"):
    res += 2
    s = s[1:-1]
    i = 0
    while i < len(s)-1:
        if s[i] == "\\" and s[i+1] in '"\\':
            res += 1
            i += 2
        else:
            i += 1
    i = 0
    while i < len(s)-3:
        if s[i:i+2] == "\\x" and is_hex_str(s[i+2:i+4]):
            res += 3
            i += 4
        else:
            i += 1

print res # 1350

print sum(2 + sum(c in "\"\\" for c in s) for s in contents.split("\n"))