from status import Status

class Player:
    def __init__(self, name, color):
        self.piece_has = 32  # オセロのコマの所持数
        self.name = name
        self.color = Status[color]

    def put_piece(self):
        self.piece_has -= 1