def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, reverse=True, key=lambda item: item["power"])


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda item: item['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda item: f"* {item} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda item: item["power"])["power"]
    min_power = min(mages, key=lambda item: item["power"])["power"]
    avg_power = round(sum(
        map(lambda item: item["power"], mages)) / len(mages), 2)
    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power
    }


def main() -> None:
    print("\nTesting artifact sorter...")
    try:
        artifacts = [
            {"name": "Crystal Orb", "power": 85, "type": "orb"},
            {"name": "Fire Staff", "power": 92, "type": "staff"}
        ]
        art_sort = artifact_sorter(artifacts)
        for i in range(len(art_sort) - 1):
            a1 = art_sort[i]
            a2 = art_sort[i + 1]
            print(f"{a1['name']} ({a1['power']} power) comes before "
                  f"{a2['name']} ({a2['power']} power)")
    except Exception as err:
        print(err)
    print("\nTesting spell transformer...")
    try:
        spells = ["fireball", "heal", "shield"]
        print(" ".join(spell_transformer(spells)))
    except Exception as err:
        print(err)


if __name__ == "__main__":
    main()
