import hashlib

inp = 'bgvyzdsv'

def find_first(target):
    i = 1
    while True:
        key = (inp + str(i)).encode('utf-8')
        out = hashlib.md5(key).hexdigest()
        if out.startswith(target):
            break
        i += 1
    return i

print(find_first('00000'), find_first('000000')) # 254575 1038736