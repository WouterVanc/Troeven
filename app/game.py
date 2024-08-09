from collections import defaultdict

from game_utils import Card, Deck, Player, Team


class Game:

    def __init__(self, players: list[Player]) -> None:
        self.players: list[Player] = players
        self.deck: Deck = Deck()
        self.dealer: Player = Player()
        self.decide_teams()

    def decide_teams(self) -> None:
        """Method to divide players into teams with 'boerke leggen' and assign the first dealer."""
        print(" --- BOERKE LEGGEN --- ")
        print(self.players[0])
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

        self.dealer: Player = self.players[removed_indices[0]]
        teams: defaultdict = defaultdict(list)
        for player_idx, player in enumerate(self.players):
            player.team = Team.ONE if player_idx in removed_indices else Team.TWO
            teams[player.team].append(player)

        teams[Team.ONE].remove(self.dealer)
        teams[Team.ONE].insert(0, self.dealer)

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
        dealer_index: int = self.players.index(self.dealer)
        new_dealer_index: int = (dealer_index + 1) % 4
        self.dealer: Player = self.players[new_dealer_index]
        print(f"New dealer = {self.dealer.name}")

    def action_order(self) -> list[Player]:
        start_index: int = self.players.index(self.dealer) + 1
        player_order: list[Player] = (
            self.players[start_index:] + self.players[:start_index]
        )
        return player_order

    def deal_cards(self) -> list[Card]:
        print(f"The current dealer = {self.dealer.name}\n")
        deal_order: list[Player] = self.action_order()

        turn: int = 0
        while len(self.deck) > 3:
            for player in deal_order:
                if not self.deck.cards:
                    break
                turn += 1
                dealt_cards: list[Card] = [self.deck.cards.pop(), self.deck.cards.pop()]
                print(
                    f"Player: {player.name} was dealt {[str(card) for card in dealt_cards]} cards at turn {turn}."
                )
                if turn == 8:
                    troev_pile: list[Card] = dealt_cards

                player.receive_cards(card=dealt_cards)

        print(f"final_deck_size = {len(self.deck)}")

        print(f"The Troev pile = {[str(card) for card in troev_pile]}\n")

        return troev_pile

    def play_or_pass(self, troev_pile: list[Card]) -> Team:
        player_order: list[Player] = self.action_order()[:-1] + self.action_order()

        turn: int = 0
        for player in player_order:
            turn += 1
            current_troev: Card = troev_pile[0] if turn < 4 else troev_pile[1]
            print(f"THE CURRENT TROEV = {current_troev}")
            print(
                f"{player.name} is currently holding: {[str(card) for card in player.cards]}"
            )
            answer: str = input("Do you want to play?")
            if answer.lower() == "yes":
                print(f"{player.team} wants to play with the troev {current_troev}")
                break

        return player.team


if __name__ == "__main__":

    game = Game(
        players=[
            Player(name="bob"),
            Player(name="josh"),
            Player(name="allen"),
            Player(name="rick"),
        ]
    )

    troev_pile: list[Card] = game.deal_cards()

    game.play_or_pass(troev_pile=troev_pile)
