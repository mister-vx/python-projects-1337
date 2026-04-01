from ex4.TournamentCard import TournamentCard
from typing import Dict


class TournamentPlatform:
    def __init__(self) -> None:
        self.cards: Dict = {}
        self.match_played = 0

    def register_card(self, card: TournamentCard) -> str:
        if "Dragon" in card.name:
            card_id = "dragon_001"
        elif "Wizard" in card.name:
            card_id = "wizard_001"
        else:
            card_id = card.name.lower().replace(" ", "_") + "_001"
        self.cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card_1 = self.cards.get(card1_id)
        card_2 = self.cards.get(card2_id)

        if not card_1 or not card_2:
            raise ValueError("Invalid cards")
        if card_1.attack_p >= card_2.attack_p:
            winr = card_1
            losr = card_2
            winr_id = card1_id
            losr_id = card2_id
        else:
            winr = card_2
            losr = card_1
            winr_id = card2_id
            losr_id = card1_id
        winr.update_wins(1)
        losr.update_losses(1)
        self.match_played += 1
        return {
            "winner": winr_id,
            "loser": losr_id,
            "winner_rating": winr.calculate_rating(),
            "loser_rating": losr.calculate_rating()
        }

    def get_leaderboard(self) -> list:
        leadbord = sorted(
            self.cards.items(),
            key=lambda item: item[1].calculate_rating(),
            reverse=True
        )
        res = []
        for cid, crd in leadbord:
            res.append({
                "id": cid,
                "name": crd.name,
                "rating": crd.calculate_rating(),
                "record": f"{crd.win}-{crd.loss}"
            })
        return res

    def generate_tournament_report(self) -> dict:
        total = len(self.cards)
        avg = (sum([card.calculate_rating()
                    for card in self.cards.values()]) / total
               if total > 0 else 0)
        return {
            "total_cards": total,
            "matches_played": self.match_played,
            "avg_rating": int(avg),
            "platform_status": "active"
        }
