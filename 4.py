import hashlib

inp = 'bgvyzdsv'

i = 1
while True:
    key = inp + str(i)
    out = hashlib.md5(key).hexdigest()
    if out.startswith('00000'):
        break
    i += 1

print i

i = 1
while True:
    key = inp + str(i)
    out = hashlib.md5(key).hexdigest()
    if out.startswith('000000'):
        break
    i += 1

print i