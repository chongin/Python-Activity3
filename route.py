from leg import Leg


class Route:
    def __init__(self, route_data: dict) -> None:
        self.trip_duration = route_data["formattedTime"]
        self.distance_in_miles = route_data["distance"]
        self.distance_in_kilos = "{:.2f}".format(self.distance_in_miles * 1.61)
        self.legs = []
        for _, leg_data in enumerate(route_data["legs"]):
            self.legs.append(Leg(leg_data))

    def display(self, orig: str, dest: str) -> dict:
        print("===================== Route ============================== ")
        print(f"Directions from {orig}")
        print(f"Dirctions to {dest}")
        print(f"Trip Duration : {self.trip_duration}")
        print(f"Miles         : {self.distance_in_miles}")
        print(f"Kilos         : {self.distance_in_kilos}")
        print("========================================================= \n")
        for _, leg in enumerate(self.legs):
            leg.display()


            