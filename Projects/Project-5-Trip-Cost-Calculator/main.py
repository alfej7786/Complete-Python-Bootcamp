print("Welcome to the Trip Cost Calculator!")
stay = input("How many days will you stay? ")
hotelCost = input("How much does hotel cost per night? $")
flightCost = input("How much does flight cost? $")
rentalCar = input("If you need rental car please enter the price otherwise enter zero. $")
expenses = input("Enter other possible expenses $")

newStay = int(stay)
newhotelCost = int(hotelCost)
newflightCost = int(flightCost)
newrentalCar = int(rentalCar)
newrExpenses = int(expenses)

t1 = newStay*newhotelCost
t2 = newStay*newrentalCar
totalExp = float(t1+t2+newflightCost+newrExpenses)

print(f"Total Cost: ${totalExp}")