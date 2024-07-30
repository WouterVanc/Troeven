from __future__ import annotations

from enum import Enum, auto
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .cards import Card


class Team(Enum):

    ONE = auto()
    TWO = auto()

    def __str__(self) -> str:
        return self.name.lower()


class Player:

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.team: Team | None = None
        self.cards: list[Card] = []

    def __str__(self) -> str:
        if self.cards == []:
            current_hand: str | list[str] = "no cards"
        else:
            current_hand: str | list[str] = [str(card) for card in self.cards]
        return f"{self.name} is part of team {str(self.team)} and currently holds {current_hand}."

    def __repr__(self) -> str:
        return f"Player:{self.name},{self.team},{self.cards}"

    def receive_cards(self, card: Card | list[Card]) -> None:
        match card:
            case Card():
                self.cards.append(card)
            case list():
                self.cards.extend(card)

    def play_card(self, card_idx: int) -> Card:
        return self.cards.pop(card_idx)


if __name__ == "__main__":
    print(repr(Team))
