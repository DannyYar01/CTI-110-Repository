#cti-110
#P4HW2- Pizza order
#Danny Yarborough
#3/24/2022




#Determine variables
def main():
##    While_going = 'yes'
    students = int(input("How many students do you want to order pizza for? "))
    pizza = int(input("Enter number of people per pizza (1.5, 2 or 3): "))

    #Declare rates
     
    overall = pizza * students
    tax_rate = .06
    i = 1
    tax = overall * tax_rate
    cost =  overall + tax
    total_pizzas = students / pizza 
    while i == 1:
    #If statements
        if pizza == 1.5:
            print("-----------pizza order--------")
            print("Number of students: ",students)
            print("Pizzas needed: ",)
            print("Price", cost)
        elif pizza == 2:
            print("-----------pizza order--------")
            print("Number of students: ",students)
            print("Pizzas needed: ",total_pizzas)
            print("Price", cost)
        elif pizza == 3:
            print("-----------pizza order--------")
            print("Number of students: ",students)
            print("Pizzas needed: ",total_pizzas)
            print("Price", cost)

        else:
            print("INVALID ENTRY!!!!\nSHOULD HAVE ENTERED 1.5, 2 or 3")
        v = input("Enter yes to run the program again: ")
        if v != "yes":
            i = i+1
            print("Program TERMINATED")
        

main()



