import math

class ParkingTicket:
    def __init__(self, car, meter, officer_name, badge_number):
        self.car = car
        self.meter = meter
        self.officer_name = officer_name
        self.badge_number = badge_number
        self.fine = self.calculate_fine()

    def calculate_fine(self):
        overtime = self.car.minutes_parked - self.meter.minutes_purchased

        if overtime <= 0:
            return 0

        hours = math.ceil(overtime / 60)

        if hours == 1:
            return 25
        else:
            return 25 + (hours - 1) * 10

    def display_ticket(self):
        print("\n--- Parking Ticket ---")
        print(f"Car: {self.car}")
        print(f"Minutes Parked: {self.car.minutes_parked}")
        print(f"Minutes Purchased: {self.meter.minutes_purchased}")
        print(f"Fine: ${self.fine:.2f}")
        print(f"Issued by Officer: {self.officer_name} (Badge {self.badge_number})")
        print("----------------------")



