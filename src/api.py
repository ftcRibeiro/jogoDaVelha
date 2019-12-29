from http import HTTPStatus
from flask_restful import Resource, Api
from flask import Flask, request as rq, make_response
import importlib as imp
import sys
import json
import service as srv
import utilities as utl
import dataInterface as db
import validation as vld
app = Flask(__name__)
api = Api(app)

@app.route('/game', methods=['POST'])
def newGame():
    headers = {"Content-Type": "application/json"}
    try:
        jsonData = srv.newGame()
        response = make_response(jsonData,HTTPStatus.OK)
        return response
    except Exception as e:
        jsonData = {
            "exception": str(type(e).__name__),
            "message": e.args[0]
        }
        response = make_response(jsonData,HTTPStatus.BAD_REQUEST)
        return response
    
   
@app.route('/game/movement',methods=['POST'])
def newMovement():
    headers = {"Content-Type": "application/json"}
    try:
        body = rq.json
        
        if vld.isBodyValid(body):
            print(body.keys())
            jsonData, status = srv.doMovement(body)
            response = make_response(jsonData, status)
        else:
            jsonData = {
                "msg": "Formato de Body inválito para esta requisição"
            }
            response = make_response(jsonData, HTTPStatus.BAD_REQUEST)
        return response
    except Exception as e:
        jsonData = {
            "exception": str(type(e).__name__),
            "message": e.args[0]
        }
        response = make_response(jsonData,HTTPStatus.BAD_REQUEST)
        return response


if __name__ == '__main__':
    print ("\n By Felipe Ribeiro\n")
    print("\n https://www.linkedin.com/in/felipe-ribeiro-610635a4/")
    print("\n       __                  ____       _    __     ____         "+
        "\n      / /___  ____ _____  / __ \____ | |  / /__  / / /_  ____ _"+
        "\n __  / / __ \/ __ `/ __ \/ / / / __ `/ | / / _ \/ / __ \/ __ `/"+
        "\n/ /_/ / /_/ / /_/ / /_/ / /_/ / /_/ /| |/ /  __/ / / / / /_/ / "+
        "\n\____/\____/\__, /\____/_____/\__,_/ |___/\___/_/_/ /_/\__,_/  "+
        "\n           /____/                                              ")
    print("\n Tic-tac-toe simulator backend"+"\n")
    app.run()