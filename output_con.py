import output_interface
import pyfiglet
import rich
from rich.console import Console

__all__ = ["OutputCon"]


class OutputCon(output_interface.OutoutInterface):

    def __init__(self):
        self.console = Console()

    def show_welcome(self):
        self.console.print("\nAuthor: WojciechSkumajTo\n",
                           style="bold green", justify="center")
        rich.print(pyfiglet.figlet_format("XOXOXO", font="banner3-D"))

    def show_board(self, board):
        self.console.print("[bold blue]%c[/bold blue] | [bold blue]%c[/bold blue] | [bold blue]%c[/bold blue]\n"
                           "[bold red]---+---+--[/bold red]\n"
                           "%c | %c | %c\n"
                           "[bold red]---+---+--[/bold red]\n"
                           "%c | %c | %c\n" % tuple(board), justify="left")

    def show_player_turn(self, player):
        self.console.print(
            f"Now moves (0-8): {player}", style="bold green", justify="left")

    def show_move_error(self, player):
        self.console.print(
            "It's a no what you've done! Please repeat the move.", style="bold red")

    def show_draw(self):
        self.console.print("It's draw! Nobody wins!", style="red")

    def show_winner(self, player):
        self.console.print(
            f"PLayer {player} [bold blue]CONGRATULATION![/bold blue]\n")
