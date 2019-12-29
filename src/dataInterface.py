import csv
import os
from os import path
DATABASE = 'src/database/'
def createGame(game):
    fileName = DATABASE + game['id'] +'.csv'
    with open(fileName,'w',newline='') as file:
        writer = csv.writer(file)
        file.write('player,x,y,nextPlayer')
        file.write('\n,,,%s'%game['firstPlayer'])

def isGame(gameId):
    name = DATABASE+gameId + '.csv'
    fileExists = path.exists(name)
    return fileExists
    # for root, dirs, files in os.walk(DATABASE):
    #     if name in files:
    #         return True
    #     else:
    #         return False

def finishedGame(gameId):
    # lastLine = _readLastLine(DATABASE + gameId + '.csv')
    return False

def getGameResult(game):
    pass
    
def setMovement(mov):
    if mov['player']== 'X':
        nextPlayer = 'O'
    else:
        nextPlayer = 'X'
    fileName = DATABASE + mov['id']+'.csv'
    with open(fileName,'a') as file:
        file.write('\n%s,%s,%s,%s'%(mov['player'],mov['position']['x'],
                    mov['position']['y'],nextPlayer))
def isTurn(gameId, player):
    fileName = DATABASE + gameId + '.csv'
    lastLine = _readLastLine(fileName)
    if player == lastLine[3]:
        return True
    else:
        return False

def _readLastLine(fileName):
    with open(fileName) as file:
        last_line = file.readlines()[-1]
        return last_line.split(',')