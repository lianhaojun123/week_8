from silver_service_taxi import SilverServiceTaxi

def main():

    test_car = SilverServiceTaxi("Test Car", 200, 2)
    test_car.drive(18)
    print(test_car)

main()