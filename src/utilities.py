import string
import random

def genGameId(chars=string.digits + string.ascii_letters ):
    key1 = ''.join(random.choice(chars) for _ in range(8))
    key2 = '-'+''.join(random.choice(chars) for _ in range(4))
    key3 = '-'+''.join(random.choice(chars) for _ in range(4))
    key4 = '-'+''.join(random.choice(chars) for _ in range(4))
    key5 = '-'+''.join(random.choice(chars) for _ in range(12))
    key = key1+key2+key3+key4+key5
    return key

def genFirst():
    return random.choice('X'+'O')


