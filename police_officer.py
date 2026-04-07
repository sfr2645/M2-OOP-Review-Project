from parking_ticket import ParkingTicket

class PoliceOfficer:
    def __init__(self, name, badge_number):
        self.name = name
        self.badge_number = badge_number

    def inspect_car(self, car, meter):
        if car.minutes_parked > meter.minutes_purchased:
            return ParkingTicket(car, meter, self.name, self.badge_number)
        else:
            return None

