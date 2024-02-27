from models.board import Board
from models.player import Player

class Game:
    def __init__(self):
        self.p1 = Player("Player1", "WHITE")
        self.p2 = Player("Player2", "BLACK")
        self.board = Board()

    def finish_game(self):
        if self.board.BLACK_is_win() is not None:
            if self.board.BLACK_is_win():
                print("黒が勝ちです。")
            if not self.board.BLACK_is_win():
                print("白が勝ちです。")
        if self.board.BLACK_is_win() is None:
            print("引き分けです。")
        exit()  # これってメモリ解放してくれるん...?

    def turn(self, player):
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

            self.board.set_piece_to(px, py, player.color)
            break

    def play_game(self):
        self.board.set_piece_to(3, 3, "BLACK")
        self.board.set_piece_to(4, 4, "BLACK")
        self.board.set_piece_to(3, 4, "WHITE")
        self.board.set_piece_to(4, 3, "WHITE")
        # print(id(self.board.board))
        print(self.board + "\nゲームスタート!\n(qでゲームを中断して終了します)")

        while (self.p1.piece_has != 0) and (self.p1.piece_has != 0):
            self.turn(self.p1)
            self.board.update()
            print(self.board)

            self.turn(self.p2)
            self.board.update()
            print(self.board)

        self.finish_game()

if __name__ == "__main__":
    g = Game()
    g.play_game()