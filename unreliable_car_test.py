from unreliable_car import UnreliableCar

def main():
    unreliable_car = UnreliableCar("unreliable Car", 100, 10)
    reliable_car = UnreliableCar("reliable Car", 100, 80)

    for i in range(1,5):
        print("{} drive - {}km".format(reliable_car.name, reliable_car.drive(i)))
        print("{} drive - {}km".format(unreliable_car.name, unreliable_car.drive(i)))


    print(unreliable_car)
    print(reliable_car)

main()
