from parked_car import ParkedCar
from parking_meter import ParkingMeter
from police_officer import PoliceOfficer

def run_scenario(description, car, meter, officer):
    print(f"\n== {description} ==")
    ticket = officer.inspect_car(car, meter)

    if ticket:
        ticket.display_ticket()
    else:
        print(f"{car} is legally parked. No ticket was issued.")


def main():
    # Scenario 1: Legal parking
    car1 = ParkedCar("Toyota", "Camry", "Red", "XYZ123", 30)
    meter1 = ParkingMeter(40)
    officer1 = PoliceOfficer("John Doe", "5678")

    run_scenario("Scenario 1: Legal Parking", car1, meter1, officer1)

    # Scenario 2: Illegal (less than 1 hour over)
    car2 = ParkedCar("Honda", "Accord", "Blue", "ABC987", 70)
    meter2 = ParkingMeter(60)
    officer2 = PoliceOfficer("Jane Smith", "1234")

    run_scenario("Scenario 2: Less Than 1 Hour Over", car2, meter2, officer2)

    # Scenario 3: Illegal (multiple hours over)
    car3 = ParkedCar("Ford", "Mustang", "Black", "LMN456", 190)
    meter3 = ParkingMeter(60)
    officer3 = PoliceOfficer("James Brown", "4321")

    run_scenario("Scenario 3: Multiple Hours Over", car3, meter3, officer3)

    # Scenario 4: Multiple cars
    print("\n=== Scenario 4: Parking Lot Inspection ===")
    officer4 = PoliceOfficer("Sarah Green", "9999")

    cars = [
        (ParkedCar("Nissan", "Altima", "White", "JKL321", 60), ParkingMeter(60)),
        (ParkedCar("Chevy", "Malibu", "Silver", "QWE789", 80), ParkingMeter(60)),
        (ParkedCar("BMW", "X5", "Black", "BMW111", 50), ParkingMeter(60)),
        (ParkedCar("Kia", "Soul", "Green", "KIA222", 75), ParkingMeter(60)),
        (ParkedCar("Tesla", "Model 3", "White", "TES333", 200), ParkingMeter(60)),
    ]

    for car, meter in cars:
        ticket = officer4.inspect_car(car, meter)
        if ticket:
            ticket.display_ticket()
        else:
            print(f"{car} is legally parked. No ticket was issued.")


if __name__ == "__main__":
    main()
