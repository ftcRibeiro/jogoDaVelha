import string
import ramdom

def genGameId((chars=string.ascii_uppercase + string.digits):
    key1 = ''.join(random.choice(chars) for _ in range(8))
    key2 = '-'.join(random.choice(chars) for _ in range(4))
    key3 = '-'.join(random.choice(chars) for _ in range(4))
    key4 = '-'.join(random.choice(chars) for _ in range(4))
    key5 = '-'.join(random.choice(chars) for _ in range(12))
    key = key1+key2+key3+key4+key5
    return key

def genFirst():
    return ramdom.choice('X', 'O')
