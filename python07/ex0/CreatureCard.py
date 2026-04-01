from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        if health <= 0 or attack <= 0:
            raise ValueError("health and attack must be positive integers")
        self.attack = attack
        self.health = health

    def get_card_info(self) -> dict:
        card_info = super().get_card_info()
        card_info.update(
            {"attack": self.attack,
             "health": self.health}
        )
        return card_info

    def play(self, game_state: dict) -> dict:
        game_state.setdefault("battlefield", []).append(self.name)
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target: str) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }
