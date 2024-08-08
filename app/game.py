from cards import Deck
from players import Player, Team


class Game:

    def __init__(self, players: list[Player]) -> None:
        self.players: list[Player] = players
        self.deck: Deck = Deck()
        self.dealer: int = 0

    def decide_teams(self) -> None:
        self.deck.shuffle()
        current_index: int = 0
        removed_indices: list[int] = []
        for card in self.deck:
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

        self.dealer = removed_indices[0]

    def move_dealer(self) -> None:
        self.dealer = (self.dealer + 1) % 4
        print(f"New dealer = {self.players[self.dealer]}")

    def deal_cards(self) -> None:
        start_index: int = self.dealer
        players_ordered: list[Player] = (
            self.players[start_index:] + self.players[:start_index]
        )

        c = 0
        while len(self.deck.cards) > 3:
            for player in players_ordered:
                c += 1
                if c > start_index:
                    print(f"Player: {player.name} was dealt 2 cards.")
                    player.receive_cards(
                        card=[self.deck.cards.pop(), self.deck.cards.pop()]
                    )


if __name__ == "__main__":

    # Create players
    game = Game(
        players=[
            Player(name="bob"),
            Player(name="josh"),
            Player(name="allen"),
            Player(name="rick"),
        ]
    )

    game.decide_teams()
    print("\n")
    game.deal_cards()
