from http import HTTPStatus
from flask_restful import Resource, Api
from flask import Flask, request as rq, make_response
import importlib as imp
import sys
import json
import utilities as utl
import validation as vld
import dataInterface as db
app = Flask(__name__)
api = Api(app)

@app.route('/game', methods=['POST'])
def newGame():
    headers = {"Content-Type": "application/json"}
    gameId = utl.genGameId()
    firstPlayer = utl.genFirst()
    jsonData = {
        "id":gameId,
        "firstPlayer": firstPlayer
    }
    response = make_response(jsonData,HTTPStatus.OK)
    return response
   
@app.route('/game/<id>/movement',methods=['POST'])
def newMovement(id):
    headers = {"Content-Type": "application/json"}
    try:
        body = rq.json
        gameId = body['id']
        player = body['player']
        position = body['position']
        if not vld.isGame(gameId):
            jsonData = {
                "msg": "Partida não encontrada"
            }
            response = make_response(jsonData,HTTPStatus.BAD_REQUEST)
            return response

        if not vld.isTurn(player):
            jsonData = {
                "msg": "Não é turno do jogador"
            }
            response = make_response(jsonData,HTTPStatus.BAD_REQUEST)
            return response
        if vld.finishedGame(gameId):
            jsonData = vld.getGameResult(gameId)
            response = make_response(jsonData,HTTPStatus.BAD_REQUEST)
            return response
        else:
            stsMov = db.setMovement(body)
            if stsMov: #partida ainda não acabou
                jsonData = {
                    "msg": "Jogada Registrada com sucesso"
                }
                response = make_response(jsonData,HTTPStatus.OK)
                return response
            else: #esta foi a ultima jogada possível
                jsonData = vld.getGameResult(gameId)
                response = make_response(jsonData,HTTPStatus.OK)
                return response

        response = make_response('jsonData',HTTPStatus.OK)
        return response 
    except Exception as e:
        jsonData = {
            "exception": str(type(e).__name__),
            "message": e.args[0]
        }
        response = make_response(jsonData,HTTPStatus.BAD_REQUEST)
        return response


if __name__ == '__main__':
    print("\n       __                  ____       _    __     ____         "+
        "\n      / /___  ____ _____  / __ \____ | |  / /__  / / /_  ____ _"+
        "\n __  / / __ \/ __ `/ __ \/ / / / __ `/ | / / _ \/ / __ \/ __ `/"+
        "\n/ /_/ / /_/ / /_/ / /_/ / /_/ / /_/ /| |/ /  __/ / / / / /_/ / "+
        "\n\____/\____/\__, /\____/_____/\__,_/ |___/\___/_/_/ /_/\__,_/  "+
        "\n           /____/                                              ")
    print("\n Tic-tac-toe simulator backend"+"\n\n")
    app.run()