class Maneuver:
    def __init__(self, maneuver_data) -> None:
        self.index = maneuver_data['index']
        self.distance = maneuver_data['distance']
        self.narrative = maneuver_data['narrative']
        self.directionName = maneuver_data['directionName']
        self.streets = maneuver_data['streets']
        
    def display(self) -> None:
        distance_in_kilo = "{:.2f}".format(self.distance * 1.61)
        print(f"{self.narrative}. ({distance_in_kilo} km) ")