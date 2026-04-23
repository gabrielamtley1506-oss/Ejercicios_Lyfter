class Person:

    def __init__(self):
        pass

class Bus:
    def __init__(self, storage_size, passengers=None):
        self.max_passengers=storage_size
        self.passengers=passengers if passengers is not None else []
        

    def add_passenger(self, passenger):
        if not isinstance(passenger, Person):
            print("Error: passenger must be a Person object")
            return
        if len(self.passengers) >= self.max_passengers:
            print("The Bus is full")
            return
        self.passengers.append(passenger)
        print("Passenger added successfully")

    def remove_passenger(self, passenger=None):
        if passenger is None:
            if len(self.passengers) == 0:
                print("The bus is empty")
                return
            self.passengers.pop()
            print("Last passenger removed successfully")
            return
        
        if not isinstance(passenger, Person):
            print("Error: passenger must be a Person object")
            return
        
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

print("Adding passenger 4 (should fail - bus full)...")
bus.add_passenger(passenger4)
print(f"Passengers: {len(bus.passengers)}\n")

print("Trying to add an invalid object...")
bus.add_passenger("not a person")
print(f"Passengers: {len(bus.passengers)}\n")

print("Removing last passenger (no object needed)...")
bus.remove_passenger()
print(f"Passengers after removal: {len(bus.passengers)}\n")

print("Removing specific passenger...")
bus.remove_passenger(passenger1)
print(f"Passengers after removal: {len(bus.passengers)}")

print("Removing passenger 2...")
bus.remove_passenger(passenger2)
print(f"Passengers: {len(bus.passengers)}")