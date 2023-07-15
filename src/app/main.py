from fastapi import FastAPI
from mangum import Mangum
from src.app.shared.domain.entities.battlesnake import Battlesnake
import random
from src.app.shared.domain.entities.board import Board

app = FastAPI()

@app.get('/')
def get_root():
    response = {
        "apiversion": "1",
        "author": "Briqz23",
        "color": "#9370DB",
        "head": "beluga",
        "tail": "fat-rattle",
        "version": "0.0.1-beta"
        }
    return response


@app.post('/start')
def post_start (request: dict):

    board = Board.from_json(request["'board"])
    you = Battlesnake.from_json(request["you"])

    return

@app.post('/move')
def post_move (request: dict):
    
    board = Board.from_json(request["board"])
    you = Battlesnake.from_json(request["you"])

    moves = ['up','down','right','left']
    move = random.choice(moves) #criar alguma lógica dps
    response = {
        "move": move,
        "shout":'AaAAAaaa'
    }
    return response


@app.post('/end')
def post_end(request: dict):
    print("GAME OVER")


handler = Mangum(app, lifespan="off")
