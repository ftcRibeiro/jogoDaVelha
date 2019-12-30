import csv
import os
from os import path
from http import HTTPStatus
import pandas as pd
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

def getGameResult(gameId):
    fileName = DATABASE+gameId+'.csv'
    gameData = pd.read_csv(fileName)
    playerO = gameData.loc[gameData.player=='O'].loc[:,'x':'y']
    playerX = gameData.loc[gameData.player=='X'].loc[:,'x':'y']
    return {}, 'aberto'
    
def setMovement(mov):
    fileName = DATABASE + mov['id']+'.csv'
    if _validMovement(mov,fileName):
        if mov['player']== 'X':
            nextPlayer = 'O'
        else:
            nextPlayer = 'X'
        
        with open(fileName,'a') as file:
            file.write('\n%s,%s,%s,%s'%(mov['player'],mov['position']['x'],
                        mov['position']['y'],nextPlayer))
        jsonData = {
                "msg": "Jogada Registrada com sucesso"
            }
        return jsonData, HTTPStatus.OK
    else:
        jsonData = {
                "msg": "Não é possível fazer essa jogada. Campo já preenchido"
            }
        return jsonData, HTTPStatus.BAD_REQUEST

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

def _validMovement(mov,fileName):
    fileLines = []
    with open(fileName,'r') as file:
        fileLines.append([line.split() for line in file])
    for line in fileLines[0]:
        lineData = line[0].split(',')
        if lineData[1] == str(mov['position']['x']) and lineData[2] == str(mov['position']['y']):
            return False
    return True