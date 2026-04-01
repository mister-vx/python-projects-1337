import random
from typing import List
from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity

if __name__ == "__main__":
    try:
        print("\n=== DataDeck Card Foundation ===\n")
        print("Testing Abstract Base Class Design:\n")
        creature_card = CreatureCard("Fire Dragon",
                                     5, Rarity.LEGENDARY.value, 7, 5)
        print("CreatureCard Info:")
        print(creature_card.get_card_info())
        nb_mana = 6
        print(f"\nPlaying {creature_card.name} with {nb_mana} mana available:")
        print("Playable:", creature_card.is_playable(nb_mana))
        print("Play result:", creature_card.play({}))
        targets: List[str] = ["Goblin Warrior", "Enemy Hero"]
        target = random.choice(targets)
        print(f"\n{creature_card.name} attacks {target}:")
        print("Attack result:", creature_card.attack_target(target))
        nb_mana = 3
        print(f"\nTesting insufficient mana ({nb_mana} available):")
        print("Playable:", creature_card.is_playable(nb_mana))
        print("\nAbstract pattern successfully demonstrated!")
    except Exception as err:
        print(err)
