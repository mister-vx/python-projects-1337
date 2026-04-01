from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine

if __name__ == "__main__":
    try:
        print("\n=== DataDeck Game Engine ===\n")
        print("Configuring Fantasy Card Game...")
        fantasy_card_factory = FantasyCardFactory()
        aggressive_strategy = AggressiveStrategy()
        print("Factory:", fantasy_card_factory.__class__.__name__)
        print("Strategy:", aggressive_strategy.get_strategy_name())
        print("Available types:", fantasy_card_factory.get_supported_types())
        game_engine = GameEngine()
        game_engine.configure_engine(fantasy_card_factory, aggressive_strategy)
        print("\nSimulating aggressive turn...")
        hand = [
            fantasy_card_factory.create_creature(),
            fantasy_card_factory.create_artifact(),
            fantasy_card_factory.create_spell()
        ]
        print("Hand: [%s]" % ", ".join([f"{i.name} ({i.cost})" for i in hand]))
        print("\nTurn execution:")
        hand.pop(0)
        res = aggressive_strategy.execute_turn(hand, [])
        print(f"Strategy: {aggressive_strategy.get_strategy_name()}")
        print(f"Actions: {res['actions']}")
        game_engine.simulate_turn()
        status = game_engine.get_engine_status()
        print("\nGame Report:")
        print(status)
        print("\nAbstract Factory + Strategy "
              "Pattern: Maximum flexibility achieved!")
    except Exception as err:
        print(err)
