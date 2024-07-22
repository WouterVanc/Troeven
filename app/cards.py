from __future__ import annotations

import random
from typing import TYPE_CHECKING, Self

if TYPE_CHECKING:
    from .players import Player


class Card:
    def __init__(self, suit: str, rank: int) -> None:
        self.suit: str = suit
        self.rank: int = rank

    def __str__(self) -> str:
        court_cards_map: dict[int, str] = {
            11: "Jack",
            12: "Queen",
            13: "King",
            14: "Ace",
        }
        return f"{court_cards_map.get(self.rank, self.rank)} of {self.suit}"

    def __repr__(self) -> str:
        return f'({self.rank},"{self.suit}")'


class Deck:
    def __init__(self) -> None:
        suits: list[str] = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks: list[int] = [i for i in range(9, 15)]

        self.cards: list[Card] = [
            Card(suit=suit, rank=rank) for suit in suits for rank in ranks
        ]

    def __str__(self) -> str:
        current_deck: list[str] = [str(card) for card in self.cards]
        return f"{current_deck}"

    def __repr__(self) -> str:
        return f"{self.cards}"

    def __iter__(self) -> Self:
        self.index = 0
        return self

    def __next__(self) -> Card:
        if self.index < len(self.cards):
            item: Card = self.cards[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

    def shuffle(self) -> None:
        random.shuffle(x=self.cards)

    def lift_deck(self) -> None:
        split_index: int = random.randint(a=0, b=23)
        self.cards: list[Card] = self.cards[split_index:] + self.cards[:split_index]


class Pile:

    def __init__(self) -> None:
        self.current_pile: list[tuple[Player, Card]] = []
        self.team_one_pile: list[list[Card]] = []
        self.team_two_pile: list[list[Card]] = []

    def __str__(self) -> str:
        current_pile: list[str] = [str(card) for card in self.current_pile]
        team_one_pile: list[str] = [str(card) for card in self.team_one_pile]
        team_two_pile: list[str] = [str(card) for card in self.team_two_pile]
        return f"The current pile = {current_pile}. Team one has won: {team_one_pile} and team two has won: {team_two_pile}"

    def __repr__(self) -> str:
        return f"{self.current_pile}, {self.team_one_pile}, {self.team_two_pile}"

    def add_to_current_pile(self, player: Player, card: Card) -> None:
        self.current_pile.append((player, card))
