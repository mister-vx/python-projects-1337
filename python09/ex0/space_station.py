from pydantic import BaseModel, ValidationError, Field  # type: ignore
from datetime import datetime
from typing import Optional


# BaseModel is the core class in Pydantic used to create data models
# Pydantic model representing a space station with validated operational data
class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = Field(...)
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    # Create a valid space station instance
    space_station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime.now()
    )
    print("Valid station created:")
    print("ID:", space_station.station_id)
    print(f"Name: {space_station.name}")
    print(f"Crew: {space_station.crew_size} people")
    print(f"Power: {space_station.power_level}%")
    print(f"Oxygen: {space_station.oxygen_level}%")
    print("Status: Operational"
          if space_station.is_operational else "Status: Non-operational")
    print("\n========================================")
    try:
        # Create invalid space station instance
        space_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=21,
            power_level=0.0,
            oxygen_level=92.3,
            last_maintenance=datetime.now()
        )
    except ValidationError as err:
        print("Expected validation error:")
        for e in err.errors():
            print(e["msg"])


if __name__ == "__main__":
    main()
