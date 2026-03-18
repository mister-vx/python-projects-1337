if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    player1 = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    print("Player alice achievements:", player1)
    player2 = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    print("Player bob achievements:", player2)
    player3 = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
               'perfectionist'}
    print(f"Player charlie achievements: {player3}\n")
    print("=== Achievement Analytics ===")
    players = player1.union(player2, player3)
    print("All unique achievements:", players)
    print(f"Total unique achievements: {len(players)}\n")
    print("Common to all players:", player1.intersection(player2, player3))
    r1 = player1.difference(player2, player3)
    r2 = player2.difference(player1, player3)
    r3 = player3.difference(player1, player2)
    rare_achievements = r1.union(r2, r3)
    print(f"Rare achievements (1 player): {rare_achievements}\n")
    print("Alice vs Bob common:",  player1.intersection(player2))
    print("Alice unique:", player1.difference(player2))
    print("Bob unique:", player2.difference(player1))
