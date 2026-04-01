from typing import Any
from ex0.Card import Card, Rarity
from ex2.Combatable import Combatable
from ex2.EliteCard import EliteCard
from ex2.Magical import Magical


def class_methods(c: Any) -> list:
    return [i for i, j in c.__dict__.items()
            if callable(j) and not i.startswith("__")]


if __name__ == "__main__":
    try:
        print("\n=== DataDeck Ability System ===\n")
        print("EliteCard capabilities:")
        print("- Card:", class_methods(Card))
        print("- Combatable:", class_methods(Combatable))
        print("- Magical:", class_methods(Magical))
        elite_card = EliteCard("Arcane Warrior", 5, Rarity.EPIC.value,
                               6, 10, 8)
        print(f"\nPlaying {elite_card.name} (Elite Card):\n")
        print("Combat phase:")
        print("Attack result:", elite_card.attack("Enemy"))
        print("Defense result:", elite_card.defend(5))
        print("\nMagic phase:")
        print("Spell cast:", elite_card.cast_spell("Fireball",
                                                   ["Enemy1", "Enemy2"]))
        print("Mana channel:", elite_card.channel_mana(3))
        print("\nMultiple interface implementation successful!")
    except Exception as err:
        print(err)
