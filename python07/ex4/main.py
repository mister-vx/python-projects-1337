from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform
from ex0.Card import Rarity

if __name__ == "__main__":
    try:
        print("\n=== DataDeck Tournament Platform ===\n")
        print("Registering Tournament Cards...\n")
        tournament_platform = TournamentPlatform()
        dragon = TournamentCard("Fire Dragon", 5, Rarity.LEGENDARY.value, 7, 5)
        wizard = TournamentCard("Ice Wizard", 4, Rarity.EPIC.value, 5, 6)
        id1 = tournament_platform.register_card(dragon)
        id2 = tournament_platform.register_card(wizard)
        print(f"{dragon.name} (ID: {id1}):")
        interfaces = [base.__name__ for base in dragon.__class__.__bases__]
        print(f"- Interfaces: [{', '.join(interfaces)}]")
        print(f"- Rating: {dragon.calculate_rating()}")
        print(f"- Record: {dragon.win}-{dragon.loss}")
        print(f"\n{wizard.name} (ID: {id2}):")
        print(f"- Interfaces: [{', '.join(interfaces)}]")
        print(f"- Rating: {wizard.calculate_rating()}")
        print(f"- Record: {wizard.win}-{wizard.loss}")
        print("\nCreating tournament match...")
        match = tournament_platform.create_match(id1, id2)
        print(f"Match result: {match}")
        print("\nTournament Leaderboard:")
        leader = tournament_platform.get_leaderboard()
        for i, j in enumerate(leader, start=1):
            print(f"{i}. {j['name']} - Rating: {j['rating']} ({j['record']})")
        print("\nPlatform Report:")
        report = tournament_platform.generate_tournament_report()
        print(report)
        print("\n=== Tournament Platform Successfully Deployed! ===")
        print("All abstract patterns working together harmoniously!")
    except Exception as err:
        print(err)
