import utilities as utl
import dataInterface as db
from http import HTTPStatus

def newGame():
    """
        Camada de serviços para a criação de uma nova partida

        Retornos:
        --------
        Retorna id da partida e marcador do jogador a iniciar, em formato de dict
            {
                "id": gameId
                "firstPlayer": firtsPlayer
            }
    """
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
    """
        Camada de serviços para a realização de uma nova jogada

        Parâmetros:
        -----------
        Recebe dict mov com o dados da jogada, no formato:
            {
                "id" : "fbf7d720-df90-48c4-91f7-9462deafefb8",
                "player": "X",
                "position": {
                    "x": 0,
                    "y": 1
                }
            }


        Retornos:
        ---------
        Retorna uma lista, sendo o primeiro item o json com dados de mensagem:
            {
                "msg": "Jogada Registrada com sucesso"
            }
        E o segundo item a resposta HTTP correspondente
    """
    try:
        gameId = mov['id']
        player = mov['player']
        if not db.isGame(gameId):
            jsonData = {
                "msg": "Partida não encontrada"
            }
            return jsonData, HTTPStatus.BAD_REQUEST
        
        if not db.isTurn(gameId,player):
            jsonData = {
                "msg": "Não é turno do jogador"
            }
            return jsonData, HTTPStatus.BAD_REQUEST

        
        jsonData, sts = db.getGameResult(gameId)
        if sts == 'terminado':
            return jsonData, HTTPStatus.BAD_REQUEST
        else:
            jsonData, status = db.setMovement(mov)
            
            return jsonData, status
    except Exception as e:
        raise e