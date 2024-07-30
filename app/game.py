from cards import Deck
from players import Player


class Game:

    def __init__(self, players: list[Player]) -> None:
        self.players: list[Player] = players

    def decide_teams(self) -> None:
        deck: Deck = Deck()
        deck.shuffle()

        current_index: int = 0
        removed_indices: list[int] = []
        c = 0
        for card in deck:
            c += 1

            if len(removed_indices) == 2:
                break

            print(f"current card {card}")
            while current_index in removed_indices:
                current_index += 1

            print(
                f"current index = {current_index} so the card has been given to {self.players[current_index].name}"
            )

            if card.rank == 11:
                removed_indices.append(current_index)

            if c == 4:
                print("\n")
                c = 0

            current_index = (current_index + 1) % 4

        print("finished")
        print(f"team one = {[self.players[idx].name for idx in removed_indices]}")


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
