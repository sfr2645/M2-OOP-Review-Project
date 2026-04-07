class ParkedCar:
    def __init__(self, make, model, color, license_number, minutes_parked):
        self.make = make
        self.model = model
        self.color = color
        self.license_number = license_number
        self.minutes_parked = minutes_parked

    def __str__(self):
        return f"{self.color} {self.make} {self.model} ({self.license_number})"



