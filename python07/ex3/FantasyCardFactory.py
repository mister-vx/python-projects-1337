from ex0.Card import Card, Rarity
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def create_creature(self,
                        name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            return CreatureCard(name_or_power, 5, Rarity.LEGENDARY.value, 7, 5)
        elif isinstance(name_or_power, int):
            return CreatureCard("CreatureCard", 5, Rarity.LEGENDARY.value,
                                name_or_power, 5)
        else:
            return CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY.value,
                                7, 5)

    def create_spell(self,
                     name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            return SpellCard(name_or_power, 3, Rarity.RARE.value, "damage")
        else:
            return SpellCard("Lightning Bolt", 3, Rarity.RARE.value, "damage")

    def create_artifact(self,
                        name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            return ArtifactCard(
                name_or_power, 2, Rarity.COMMON.value, 3, "+1 mana per turn"
            )
        else:
            return ArtifactCard(
                "Goblin Warrior", 2, Rarity.COMMON.value, 3, "+1 mana per turn"
            )

    def create_themed_deck(self, size: int) -> dict:
        deck = []
        for i in range(size):
            if i % 2 == 0:
                deck.append(self.create_creature())
            elif i % 2 == 1:
                deck.append(self.create_spell())
            else:
                deck.append(self.create_artifact())
        return {
            "cards": deck,
            "size": len(deck),
            "theme": "Fantasy"
        }

    def get_supported_types(self) -> dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"]
        }
