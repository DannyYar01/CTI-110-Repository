# Programming inputs for a pizza delivery for a class
    # 2/13/2022
    # CTI-110 P1HW2 - Pizza Order
    # Danny Yarborough
#Number of students 20
students = int(input("How many students do you want to order pizza for:"))
print()
#number of slices 3 slices per
slices = 3 * students
#number of pizzas 1 pizza per 2 students
pizza = students / 2

print("---- Pizza Order----")
print("Number of students:", students)
print("Number of pizza slices:", slices)
print("Pizzas Needed :", pizza)
print("--------------------------")
#putting input here for the file not to auto close
input()

