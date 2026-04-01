import random

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        if attack <= 0 or health <= 0:
            raise ValueError("Attack and health must be positive integers")

        self.attack_p = attack
        self.health = health
        self.win = 0
        self.loss = 0

    def play(self, game_state: dict) -> dict:
        game_state.setdefault("tournament_zone", []).append(self.name)
        effect = random.choice([
            "enters with a roar",
            "Emits magical energy"
        ])
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Tournament card played ({effect})"
        }

    def attack(self, target: str) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_p
        }

    def defend(self, incoming_damage: int) -> dict:
        self.health -= incoming_damage
        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "remaining_health": self.health
        }

    def calculate_rating(self) -> int:
        base = 1200 if "Dragon" in self.name else 1150
        return base + (self.win * 16) - (self.loss * 16)

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_p,
            "health": self.health
        }

    def update_wins(self, wins: int) -> None:
        self.win += wins

    def update_losses(self, losses: int) -> None:
        self.loss += losses

    def get_rank_info(self) -> dict:
        return {
            "wins": self.win,
            "losses": self.loss,
            "rating": self.calculate_rating()
        }

    def get_tournament_stats(self) -> dict:
        return {
            "name": self.name,
            "attack": self.attack_p,
            "health": self.health,
            **self.get_rank_info()
        }
