from status import Status

class Piece:

    def __init__(self, x, y):
        self.state = Status.SPACE.value #初期状態では全ての目が"・"
        self.x = x
        self.y = y

    def set_state(self, color):
        self.state = Status[color].value
        

    def reverse_piece(self):  # 裏返す
        if self.state == Status.BLACK.value:
            self.state = Status.WHITE.value
        elif self.state == Status.WHITE.value:
            self.state = Status.BLACK.value
        else:
            self.state = Status.SPACE.value

    def __str__(self):
        return self.state