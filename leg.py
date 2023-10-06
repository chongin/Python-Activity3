from maneuver import Maneuver


class Leg:
    def __init__(self, leg_data: dict) -> None:
        self.index = leg_data['index']
        self.distance_in_miles = leg_data['distance']
        self.maneuvers = []
        for _, maneuver_data in enumerate(leg_data['maneuvers']):
            self.maneuvers.append(Maneuver(maneuver_data))
        pass

    def display(self) -> None:
        print("===================== DIRECTIONS =============================")
        print(f"Leg index     : {self.index}")
        print(f"Miles         : {self.distance_in_miles}")
        print("==============================================================")
        for _, maneuver in enumerate(self.maneuvers):
            maneuver.display()

        print("\n")