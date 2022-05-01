import threading 

## function to set interval
def set_interval(func, sec): 
    def func_wrapper():
        set_interval(func, sec) 
        func()  
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

# Class Roadway that is used to create object for each roadway present in the airport 
class RoadWay : 
    def __init__(self,no:int) -> None:
        self.is_occupied = False 
        self.roadway_number = no 
        self.flight_number = None 

    # Alters Status of the roadway 
    def toggle_status(self) -> None:
        self.is_occupied = not self.is_occupied 

    # Sets flight number that is currently associated
    # with the given roadway 
    def set_flight(self,flight_no:str) -> None:
        self.flight_number = flight_no  

    # Function that clears the roadway 
    def clear_roadway(self) -> None:
        self.flight_number = None 
        self.is_occupied = False 


# Class flight to create flights that land at the airport 
class Flight:
    def __init__(self,flight_number) -> None:
        self.flight_number = flight_number 



no_of_roadways = int(input("Enter number of roadways at the airport : ")) 

# Array to store roadway objects 
roadways = []

# Array to store flights that have not yet landed
unlanded_flights = []


for i in range(no_of_roadways):
    roadways.append(RoadWay(i+1)) 


# Function to print the current status of the airport 
def print_roadway_status():
    print("\n-------### Current Roadway Status ### --------") 
    for roadway in roadways:
        print("Roadway no : " , roadway.roadway_number , " Occupied : ", roadway.is_occupied , " Flight number : " , roadway.flight_number) 


# Function to cleanup a given roadway after given time 
def clean_roadway(roadway):
    roadway.clear_roadway() 
    print("Roadway ",roadway.roadway_number," has been cleared.")
    if(len(unlanded_flights) > 0):
        f = unlanded_flights.pop(0) 
        roadway.toggle_status() 
        roadway.set_flight(f.flight_number)
        s = threading.Timer(20,clean_roadway,[roadway])
        s.start() 

set_interval(print_roadway_status,10)

while(True):
    flight_number = input("Enter flight number to be landed : ") 
    if(flight_number == '0'):
        break 
    flight = Flight(flight_number) 

    # Assigning a flight to a roadway
    for roadway in roadways:
        if not roadway.is_occupied:
            roadway.toggle_status() 
            roadway.set_flight(flight.flight_number) 
            # Setting timer to clear roadway after flight has landed 
            t = threading.Timer(20,clean_roadway, [roadway]) 
            t.start() 
            break  
        else: 
            continue 
    else:
        print("Currently there are no available roadways, please wait till all roadways have been cleared")
        unlanded_flights.append(flight) 
