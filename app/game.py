from collections import defaultdict

from game_utils import Deck, Player, Team


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

        first_dealer: Player = self.players[removed_indices[0]]
        teams: defaultdict = defaultdict(list)
        for player_idx, player in enumerate(self.players):
            player.team = Team.ONE if player_idx in removed_indices else Team.TWO
            teams[player.team].append(player)

        teams[Team.ONE].remove(first_dealer)
        teams[Team.ONE].insert(0, first_dealer)

        self.players: list[Player] = [
            teams[Team.ONE][0],
            teams[Team.TWO][0],
            teams[Team.ONE][1],
            teams[Team.TWO][1],
        ]

        print(
            f"\nThe new order at the table = {[player.name for player in self.players]}"
        )

    def move_dealer(self) -> None:
        self.dealer = (self.dealer + 1) % 4
        print(f"New dealer = {self.players[self.dealer].name}")

    def deal_cards(self) -> None:
        print(f"The current dealer = {self.players[self.dealer].name}")
        start_index: int = self.dealer + 1
        deal_order: list[Player] = (
            self.players[start_index:] + self.players[:start_index]
        )

        while len(self.deck) > 3:
            for player in deal_order:
                if not self.deck.cards:
                    break
                print(len(self.deck))
                print(f"Player: {player.name} was dealt 2 cards.")
                player.receive_cards(
                    card=[self.deck.cards.pop(), self.deck.cards.pop()]
                )

        print(f"final_deck_size = {len(self.deck)}")

        self.move_dealer()


if __name__ == "__main__":

    # Create players
    # Imagine this is the order they sit at the table.
    game = Game(
        players=[
            Player(name="bob"),
            Player(name="josh"),
            Player(name="allen"),
            Player(name="rick"),
        ]
    )

    # 'Boerke leggen' to decide teams.
    game.decide_teams()
    print("\n")

    # Deal cards and flip the dealers card when necessary.
    game.deal_cards()
