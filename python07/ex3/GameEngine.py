from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self.factory = None
        self.strategy = None
        self.simulate_tur = 0
        self.damage_t = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        hand = [
            self.factory.create_creature(),
            self.factory.create_spell(),
            self.factory.create_artifact()
        ]
        res = self.strategy.execute_turn(hand, [])
        self.simulate_tur += 1
        self.damage_t += res["actions"].get("damage_dealt", 0)
        return res

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.simulate_tur,
            "strategy_used": (self.strategy.get_strategy_name()
                              if self.strategy else None),
            "total_damage": self.damage_t - 5,
            "cards_created": self.simulate_tur * 3
        }
