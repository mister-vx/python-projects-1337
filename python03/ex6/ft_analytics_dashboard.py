def list_comprehension(players: list[dict[str, str | int |
                                          list[str] | bool]]) -> None:
    print("=== List Comprehension Examples ===")
    high_scorers = [i["name"] for i in players if (i["score"] > 2000)]
    scores_doubled = [i["score"] * 2 for i in players]
    active_players = [i["name"] for i in players if (i["active"])]
    sort_players_names = sorted(high_scorers)
    print("High scorers (>2000):", sort_players_names)
    print("Scores doubled:", scores_doubled)
    sort_active_players = sorted(active_players)
    print("Active players:", sort_active_players)


def dict_comprehension(players: list[dict[str, str | int |
                                          list[str] | bool]]) -> None:
    print("\n=== Dict Comprehension Examples ===")
    player_scores = {i["name"]: i["score"] for i in players}
    print("Player scores:", player_scores)
    score_categories = {
        cat: len(
            [i for i in players
                if (cat == "high" and i["score"] >= 2000) or
                (cat == "medium" and 2000 <= i["score"] < 2200) or
                (cat == "low" and i["score"] < 2000)]
        )
        for cat in ["high", "medium", "low"]
    }
    print("Score categories:", score_categories)
    achievement_counts = {
        i["name"]: len(i["achievements"])
        for i in players}
    print("Achievement counts:", achievement_counts)


def set_comprehension(players: list[dict[str, str | int |
                                         list[str] | bool]]) -> None:
    print("\n=== Set Comprehension Examples ===")
    unique_players = {i["name"] for i in players}
    print("Unique players:", unique_players)
    unique_achievements = {j for i in players for j in i["achievements"]}
    print("Unique achievements:", unique_achievements)
    active_regions = {i["region"] for i in players if (i["active"])}
    print(f"Active regions: {active_regions}\n")


def combined_analysis(players: list[dict[str, str | int |
                                         list[str] | bool]]) -> None:
    print("=== Combined Analysis ===")
    print("Total players:", len(players))
    unique_achievements = {j for i in players for j in i["achievements"]}
    print("Total unique achievements:", len(unique_achievements))
    print("Average score:", sum([i["score"] for i in players]) / len(players))
    max_score = max([i["score"] for i in players])
    top_performer = [j for j in players if (j["score"] == max_score)]
    print("Top performer:", end=" ")
    for i in top_performer:
        print(
            f"{i['name']} ({i['score']} points,",
            f"{len(i['achievements'])} achievements)"
        )


if __name__ == "__main__":
    try:
        print("=== Game Analytics Dashboard ===\n")
        players = [
            {"name": "alice", "score": 2300, "active": True,
             "achievements": ['boss_slayer', 'first_kill', 'speed_demon'],
             "region": "north"},
            {"name": "bob", "score": 1800, "active": True,
             "achievements": ['level_10', 'speed_demon'],
             "region": "central"},
            {"name": "charlie", "score": 2150, "active": True,
             "achievements": ['first_kill', 'boss_slayer'],
             "region": "east"},
            {"name": "diana", "score": 2050, "active": False,
             "achievements": ['first_kill', 'speed_demon', 'collector'],
             "region": "west"}
        ]
        list_comprehension(players)
        dict_comprehension(players)
        set_comprehension(players)
        combined_analysis(players)
    except Exception as err:
        print(err)
