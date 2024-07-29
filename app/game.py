from typing import TYPE_CHECKING

from cards import Deck
from players import Player

if TYPE_CHECKING:
    from .cards import Deck
    from .players import Player


class Game:

    def __init__(self, players: list[Player]) -> None:
        self.players: list[Player] = players

    def decide_teams(self) -> None:
        deck: Deck = Deck()
        deck.shuffle()

        players_to_deal: list[Player] = self.players
        team_one: list[Player] = []
        for i_card, card in enumerate(deck):
            if len(team_one) == 2:
                team_two: list[Player] = players_to_deal
                break

            if card.rank == 11:
                current_player: Player = players_to_deal[i_card % len(players_to_deal)]
                players_to_deal.remove(current_player)
                team_one.append(current_player)

        print(
            f"team one = {[x.name for x in team_one]} and team two = {[x.name for x in team_two]}"
        )


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
