import utilities as utl
def newGame():
    gameId = utl.genGameId()
    firstPlayer = utl.genFirst()
    jsonData = {
        "id":gameId,
        "firstPlayer": firstPlayer
    }
    utl.saveGame(jsonData)
    return jsonData

def isTurn(player):
    return True

def isGame(game):
    return True

def finishedGame(game):
    return True

def getGameResult(game):
    return {
        
    }