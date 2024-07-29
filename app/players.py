from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .cards import Card


class Player:

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.team: int | None = None
        self.cards: list[Card] = []

    def __str__(self) -> str:
        return (
            f"{self.name} is part of team {self.team} and currently holds {self.cards}"
        )

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
