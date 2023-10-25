from game import Game
from gameADT import GameADT

def test_game_deve_ter_nome():
    game1 = Game("nome")
    assert game1.name == "nome"
    
def test_game_deve_ser_capaz_de_pontuar():
    game1 = Game("nome")
    game1.pontuar(10)
    game1.pontuar(20)
    assert game1.total_score == 30

def test_gameADT_deve_ser_capaz_de_pontuar():
    game2 = GameADT("nome")
    game2.pontuar(20)
    assert game2.total_score == 20

