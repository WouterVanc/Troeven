from cards import Deck
from players import Player, Team


class Game:

    def __init__(self, players: list[Player]) -> None:
        self.players: list[Player] = players

    def decide_teams(self) -> None:
        deck: Deck = Deck()
        deck.shuffle()

        current_index: int = 0
        removed_indices: list[int] = []
        for card in deck:
            if len(removed_indices) == 2:
                break

            while current_index in removed_indices:
                current_index = (current_index + 1) % 4

            print(
                f"index={current_index} -- {card} -- {self.players[current_index].name.upper()}"
            )

            if card.rank == 11:
                removed_indices.append(current_index)
                print(
                    f"{self.players[current_index].name.upper()} was given a jack and is now part of team one."
                )

            current_index = (current_index + 1) % 4

        for idx in range(4):
            if idx in removed_indices:
                self.players[idx].team = Team.ONE
            else:
                self.players[idx].team = Team.TWO

        print([str(player) for player in self.players])


if __name__ == "__main__":
    game = Game(
        players=[
            Player(name="bob"),
            Player(name="josh"),
            Player(name="allen"),
            Player(name="rick"),
        ]
    )

    game.decide_teams()
