from pydantic import (BaseModel, ValidationError,  # type: ignore
                      Field, model_validator)
from datetime import datetime
from typing import List
from enum import Enum


# Enum representing valid crew ranks in the space mission
class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


# Represents a single crew member with validated attributes
class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


# SpaceMission is a nested model that contains a list of CrewMember objects
# This allows validation of complex hierarchical data structures
class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    # Custom business rules applied after all field validation
    @model_validator(mode='after')
    def check_data_rules(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')
        if not [c for c in self.crew
                if c.rank in [Rank.commander, Rank.captain]]:
            raise ValueError(
                "Mission must have at least one Commander or Captain")
        if self.duration_days > 365:
            exp = [i for i in self.crew if i.years_experience >= 5]
            if len(exp) < (len(self.crew) / 2):
                raise ValueError("Long missions (> 365 days) need 50% "
                                 "experienced crew (5+ years)")
        if [i for i in self.crew if not i.is_active]:
            raise ValueError("All crew members must be active")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    # Creating a valid mission that satisfies all safety constraints
    space_mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime.now(),
        duration_days=900,
        budget_millions=2500.0,
        crew=[
            CrewMember(
                member_id="id_01",
                name="Sarah Connor",
                rank=Rank.commander,
                age=40,
                specialization="Mission Command",
                years_experience=16
            ),
            CrewMember(
                member_id="id_02",
                name="John Smith",
                rank=Rank.lieutenant,
                age=30,
                specialization="Navigation",
                years_experience=10
            ),
            CrewMember(
                member_id="id_03",
                name="Alice Johnson",
                rank=Rank.officer,
                age=25,
                specialization="Engineering",
                years_experience=6
            )
        ]
    )
    print("Valid mission created:")
    print(f"Mission: {space_mission.mission_name}")
    print(f"ID: {space_mission.mission_id}")
    print(f"Destination: {space_mission.destination}")
    print(f"Duration: {space_mission.duration_days} days")
    print(f"Budget: ${space_mission.budget_millions}M")
    print(f"Crew size: {len(space_mission.crew)}")
    print("Crew members:")
    for i in space_mission.crew:
        print(f"- {i.name} ({i.rank.value}) - {i.specialization}")
    print("\n=========================================")
    try:
        # INVALID MISSION
        space_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id="id_01",
                    name="Sarah Connor",
                    rank=Rank.cadet,
                    age=40,
                    specialization="Mission Command",
                    years_experience=16
                ),
                CrewMember(
                    member_id="id_02",
                    name="John Smith",
                    rank=Rank.lieutenant,
                    age=30,
                    specialization="Navigation",
                    years_experience=10
                ),
                CrewMember(
                    member_id="id_03",
                    name="Alice Johnson",
                    rank=Rank.officer,
                    age=25,
                    specialization="Engineering",
                    years_experience=6
                )
            ]
        )
    except ValidationError as err:
        print("Expected validation error:")
        for e in err.errors():
            print((e["msg"]).split(",")[-1].strip())


if __name__ == "__main__":
    main()
