import csv
import os
DATABASE = 'database/'
def createGame(game):
    fileName = DATABASE + game['id'] +'.csv'
    with open(fileName,'w',newline='') as file:
        writer = csv.writer(file)

def isGame(gameId):
    name = gameId + '.csv'
    for root, dirs, files in os.walk(DATABASE):
        if name in files:
            return True
        else:
            return False

def finishedGame(gameData):
    return True

def getGameResult(game):
    return {
    }
def setMovement(mov):
    return True

def isTurn(player):
    return True

def getGameData(gameId):
    return True