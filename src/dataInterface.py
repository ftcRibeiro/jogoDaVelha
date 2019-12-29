import csv
import os
DATABASE = 'database/'
def createGame(game):
    fileName = DATABASE + game['id'] +'.csv'
    with open(fileName,'w',newline='') as file:
        writer = csv.writer(file)
        file.write('player,x,y,nextPlayer')
        file.write('\n,,,%s'%game['firstPlayer'])

def isGame(gameId):
    name = gameId + '.csv'
    for root, dirs, files in os.walk(DATABASE):
        if name in files:
            return True
        else:
            return False

def finishedGame(gameId):
    lastLine = _readLastLine(DATABASE + gameId + '.csv')

def getGameResult(game):
    return {
    }
def setMovement(mov):
    if mov['player']== 'X':
        nextPlayer = 'O'
    else:
        nextPlayer = 'X'
    fileName = DATABASE + mov['id']+'.csv'
    with open(fileName,'wb') as file:
        file.write('\n%s,%s,%s,%s'%(mov['player'],mov['position']['x'],
                    mov['position']['y'],nextPlayer))
def isTurn(gameId, player):
    fileName = DATABASE + gameId + '.csv'
    lastLine = _readLastLine(fileName)
    if player == lastLine[3]:
        return True
    else:
        return False

def getGameData(gameId):
    return True

def _readLastLine(fileName):
    with open(fileName) as file:
        last_line = file.readlines()[-1]
        return last_line.split(',')