from ex0.CreatureCard import CreatureCard
from ex0.Card import Card
import random
from typing import List
import math
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard


class Deck:
    def __init__(self) -> None:
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        if isinstance(card, Card):
            self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise Exception("Empty List")
        card = self.cards.pop(0)
        return card

    def get_deck_stats(self) -> dict:
        creatures = 0
        spells = 0
        artifacts = 0
        avg_cost = 0
        for i in self.cards:
            if isinstance(i, CreatureCard):
                creatures += 1
            if isinstance(i, SpellCard):
                spells += 1
            if isinstance(i, ArtifactCard):
                artifacts += 1
        cost_sum = sum([i.cost for i in self.cards])
        avg_cost = (math.ceil(cost_sum / len(self.cards))
                    if len(self.cards) > 0 else 0)
        return {
            "total_cards": len(self.cards),
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": float(avg_cost)
        }
