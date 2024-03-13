from models.status import Status
from models.board import Board

class Player:
    def __init__(self, name, color):
        self.piece_has = 32  # オセロのコマの所持数
        self.name = name
        self.color = Status.label_of(color)

    def _put_piece(self):
        self.piece_has -= 1

    def choice_place(self):
        while True:
            p_puts = input("{}({})の手番です([x y]で座標を指定してください):".format(player.name, player.color))
            p_puts = p_puts.strip().split(" ")
            if p_puts[0] == 'q':
                self.finish_game()
            px = int(p_puts[0]) - 1
            py = int(p_puts[1]) - 1
            if self.board.is_already_put(px, py):
                print("その場所には既にコマが置かれています。")
                continue
            if (px < 0) or (px >= 8) or (py < 0) or (py >= 8):
                print("範囲外です。")
                continue
            break
        return px, py