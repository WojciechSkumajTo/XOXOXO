from game import Game
from output_con import OutputCon
from input_con import InputCon


class Harness():
    def __init__(self, output, inputs):
        self._output = output
        self._inputs = inputs
        self._game = Game()

    def start(self):
        self._output.show_welcome()

        while True:
            self._output.show_board(self._game.get_board())

            player_id = self._game.get_turn_no()
            player = self._game.get_turn()

            self._output.show_player_turn(player)

            while True:
                move = self._inputs[player_id].get_move()
                if move is None:
                    self._output.show_move_error(player)
                    continue

                if self._game.make_move(move) is False:
                    self._output.show_move_error(player)
                    continue

                break
            if not self._game.get_end():
                continue

            self._output.show_board(self._game.get_board())
            w = self._game.get_winner()
            if w is None:
                self._output.show_draw()
            else:
                self._output.show_winner(w)
            break


def main():
    inputcon1 = InputCon()
    inputcon2 = InputCon()
    outputcon = OutputCon()

    player_inputs = [inputcon1, inputcon2]
    player_outputs = outputcon

    h = Harness(player_outputs, player_inputs)
    h.start()


if __name__ == "__main__":
    main()
