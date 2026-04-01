from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        if (durability <= 0):
            raise ValueError("durability must be positive integer")
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        game_state.setdefault("battlefield", []).append(self.name)
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}"
        }

    def activate_ability(self) -> dict:
        return {
            "artifacts": self.name,
            "effect": self.effect,
            "durability": self.durability
        }
