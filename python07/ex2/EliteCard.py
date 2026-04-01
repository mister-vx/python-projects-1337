import random
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import List


class EliteCard(Card, Combatable, Magical):

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int, mana: int) -> None:
        super().__init__(name, cost, rarity)
        if attack <= 0 or health <= 0 or mana < 0:
            raise ValueError("Invalid stats")
        self.a_attack = attack
        self.health = health
        self.mana = mana

    def play(self, game_state: dict) -> dict:
        game_state.setdefault("battlefield", []).append(self.name)
        effects: List = ["Creature summoned to battlefield",
                         "Emits magical energy"]
        effect = random.choice(effects)
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effect
        }

    def attack(self, target: str) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.cost,
            "combat_type": "melee"
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        used = 4 if self.mana >= 4 else self.mana
        self.mana -= used
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": used
        }

    def defend(self, incoming_damage: int) -> dict:
        d_blocked = 3 if incoming_damage >= 3 else incoming_damage
        d_taken = incoming_damage - d_blocked
        self.health -= d_taken
        return {
            "defender": self.name,
            "damage_taken": d_taken,
            "damage_blocked": d_blocked,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.a_attack,
            "health": self.health
        }

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> dict:
        return {"mana": self.mana}
