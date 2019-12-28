def isBodyValid(body):
    valid = 0
    if len(body) == 3:
        valid += 1
    keyList = ['id', 'player', 'position']
    subkeyList = ['x','y']
    if all(key in body for key in keyList):
        valid += 1
    if all(subkey in body['position'] for subkey in subkeyList):
        valid += 1
    if body['position']['x']<3 and body['position']['x']>=0:
        valid += 1
    if body['position']['y']<3 and body['position']['y']>=0:
        valid += 1
    if valid == 5:
        return True
    else:
        return False