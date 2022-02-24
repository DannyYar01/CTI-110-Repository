#Calculate subtotal, sales tax and overall total
## 2/24/2022
## CTI-110 P2HW1 - Total Purchases
## Danny Yarborough
#List items
num1 = float(input("Enter the price of item #1: "))
num2 = float(input("Enter the price of item #2: "))
num3 = float(input("Enter the price of item #3: "))
num4 = float(input("Enter the price of item #4: "))
num5 = float(input("Enter the price of item #5: "))
print()
print("----------Results------")
#caluclate subtotal, tax and overall
total = (num1 + num2 + num3 + num4 + num5)
print("Subotal: ",format(total, '.2f'))

tax_rate = 0.07
tax = (total * tax_rate)
print("Sales Tax: ",format(tax, '.2f'))

overall = (total + tax)
print("Total: ",format(overall, '.2f'))
