inp = 'cqjxjnds'

# a recursive formulation for addition
def inc(s): return 'a' if s is '' else s[:-1] + chr(1 + ord(s[-1])) if s[-1] != 'z' else inc(s[:-1]) + 'a'

def is_allowed(s):
    if len(s) < 3:
        return False
    if 'i' in s or 'o' in s or 'l' in s:
        return False
    found_consec_trio = False
    for i in xrange(len(s)-2):
        if 1 == ord(s[i+1]) - ord(s[i]) == ord(s[i+2]) - ord(s[i+1]):
            found_consec_trio = True
            break
    if not found_consec_trio:
        return False
    found_pair = [False for i in xrange(26)]
    for c in 'abcdefghijklmnopqrstuvwxyz':
        if any(s[i] == s[i+1] == c for i in xrange(len(s)-1)):
            found_pair[ord(c)-97] = True
    if sum(found_pair) < 2:
        return False
    return True

out = inp
while True:
    if is_allowed(out):
        break
    out = inc(out)

print out # cqjxxyzz

out = inc(out)
while True:
    if is_allowed(out):
        break
    out = inc(out)

print out