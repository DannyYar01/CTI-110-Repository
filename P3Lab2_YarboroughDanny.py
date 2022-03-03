#declare the variables
##oil_change = 35
##tire_rotation = 19
##car_wash = 7

# work with inputs
work = input()

print("Enter desired auto service:")

print("You entered:", work)

if work == "Oil change":
    print("Cost of oil change: $35")
elif work == "Tire rotation":
    print("Cost of tire rotation: $19")
elif work == "Car wash":
    print("Cost of car wash: $7")
else:
    print("Error: Requested service is not recognized")
