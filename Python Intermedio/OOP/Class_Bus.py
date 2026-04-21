class Person:

    def __init__(self):
        pass

class Bus:
    passengers=[]
    def __init__(self, storage_size):
        self.max_passengers=storage_size
        

    def add_passenger(self, passenger):
        if len(self.passengers) >= self.max_passengers:
            print("The Bus is full")
            return
        self.passengers.append(passenger)

    def remove_passenger(self, passenger):
        if passenger in self.passengers:
            self.passengers.remove(passenger)
            print("Passenger removed successfully")
            return
        print("Passenger not found on the bus")

bus = Bus(3)  

passenger1 = Person()
passenger2 = Person()
passenger3 = Person()
passenger4 = Person()

print(f"Bus capacity: {bus.max_passengers}")
print(f"Current passengers: {len(bus.passengers)}\n")


print("Adding passenger 1...")
bus.add_passenger(passenger1)
print(f"Passengers: {len(bus.passengers)}\n")

print("Adding passenger 2...")
bus.add_passenger(passenger2)
print(f"Passengers: {len(bus.passengers)}\n")

print("Adding passenger 3...")
bus.add_passenger(passenger3)
print(f"Passengers: {len(bus.passengers)}\n")

print("Adding passenger 4 (should fail)...")
bus.add_passenger(passenger4)
print(f"Passengers: {len(bus.passengers)}")

print("Removing passenger 2...")
bus.remove_passenger(passenger2)
print(f"Passengers: {len(bus.passengers)}")