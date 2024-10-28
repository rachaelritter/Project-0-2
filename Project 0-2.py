AllowedVehiclesList = ["Ford F-150", "Chevrolet Silverado", "Tesla Cybertruck", "Toyota Tundra", "Nissan Titan"]

def menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. Exit")
    
def printVehicles():
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in AllowedVehiclesList:
        print(vehicle)
        
def searchVehicle():
    search = input("Please enter the full vehicle name: ")
    if search in AllowedVehiclesList:
        print(f"{search} is an authorized vehicle")
    else:
        print(f"{search} is not an authorized vehicle, if you received this in error please check the spelling and try again")

def main():
    while True: 
        menu()
        number = input()
        if number == "1":  
            printVehicles()
        elif number == "2":
            searchVehicle()
        elif number == "3":
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
            
if __name__ == "__main__":
    main()