import utilities as utl
import dataInterface as db
from http import HTTPStatus

def newGame():
    try:
        gameId = utl.genGameId()
        firstPlayer = utl.genFirst()
        jsonData = {
            "id":gameId,
            "firstPlayer": firstPlayer
        }
        db.createGame(jsonData)
        return jsonData
    except Exception as e:
        raise e

def doMovement(mov):
    try:
        gameId = mov['id']
        player = mov['player']
        position = mov['position']
        if not db.isGame(gameId):
                jsonData = {
                    "msg": "Partida não encontrada"
                }
                return jsonData, HTTPStatus.BAD_REQUEST

        if not db.isTurn(player):
            jsonData = {
                "msg": "Não é turno do jogador"
            }
            return jsonData, HTTPStatus.BAD_REQUEST

        if db.finishedGame(gameId):
            jsonData = db.getGameResult(gameId)
            return jsonData, HTTPStatus.BAD_REQUEST

        else:
            db.setMovement(mov)
            jsonData = {
                "msg": "Jogada Registrada com sucesso"
            }
            return jsonData, HTTPStatus.OK
    except Exception as e:
        raise e