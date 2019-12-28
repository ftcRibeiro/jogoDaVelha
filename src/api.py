from http import HTTPStatus
from flask_restful import Resource, Api
from flask import Flask, request as rq, make_response
import importlib as imp
import sys
import json
import utilities as utl
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
   
@app.route('game/<id>/movement',methods=['POST'])
def newMovement():
     headers = {"Content-Type": "application/json"}
    
    


if __name__ == '__main__':
    print("\n       __                  ____       _    __     ____         "+
        "\n      / /___  ____ _____  / __ \____ | |  / /__  / / /_  ____ _"+
        "\n __  / / __ \/ __ `/ __ \/ / / / __ `/ | / / _ \/ / __ \/ __ `/"+
        "\n/ /_/ / /_/ / /_/ / /_/ / /_/ / /_/ /| |/ /  __/ / / / / /_/ / "+
        "\n\____/\____/\__, /\____/_____/\__,_/ |___/\___/_/_/ /_/\__,_/  "+
        "\n           /____/                                              ")
    print("\n Tic-tac-toe simulator backend"+"\n\n")
    app.run()