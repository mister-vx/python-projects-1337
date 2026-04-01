import random
from typing import List
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        play_card: List = []
        temp = hand.copy()
        random.shuffle(temp)
        while temp:
            min_cost = temp[0]
            for c in temp:
                if c.cost < min_cost.cost:
                    min_cost = c
            play_card.append(min_cost)
            temp.remove(min_cost)
        used = 0
        for i in play_card:
            used += i.cost
        damage_dealt = 3
        for i in play_card:
            damage_dealt += i.cost
        targets: List = []
        if battlefield:
            for i in battlefield:
                targets.append(i.name)
        else:
            targets = ["Enemy Player"]
        return {
            "strategy": self.get_strategy_name(),
            "actions": {
                "cards_played": sorted([i.name for i in play_card]),
                "mana_used": used,
                "targets_attacked": targets,
                "damage_dealt": damage_dealt
            }
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return available_targets
