from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck
from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity

if __name__ == "__main__":
    try:
        print("\n=== DataDeck Deck Builder ===\n")
        print("Building deck with different card types...")
        spell_card = SpellCard('Lightning Bolt', 3,
                               Rarity.LEGENDARY.value, "damage")
        artifact_card = ArtifactCard('Mana Crystal', 2, Rarity.LEGENDARY.value,
                                     4, "+1 mana per turn")
        creature_card = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY.value,
                                     7, 5)
        deck = Deck()
        deck.add_card(spell_card)
        deck.add_card(artifact_card)
        deck.add_card(creature_card)
        print("Deck stats:", deck.get_deck_stats())
        print("\nDrawing and playing cards:\n")
        while deck.cards:
            card = deck.draw_card()
            if card:
                ty_card = card.__class__.__name__.replace("Card", "")
                print(f"Drew: {card.name} ({ty_card})")
                print(f"Play result:  {card.play({})}\n")
        print("Polymorphism in action: Same interface,"
              " different card behaviors!")
    except Exception as err:
        print(err)
