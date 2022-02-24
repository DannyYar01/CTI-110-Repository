##CTI-110
##P2HW2- Score Avg
##Danny Yarborough
##2/24/2022

#create a list
num_list = []
num = float(input("Enter score #1: "))
num_list.append(num)
num = float(input("Enter score #2: "))
num_list.append(num)
num = float(input("Enter score #3: "))
num_list.append(num)
num = float(input("Enter score #4: "))
num_list.append(num)
num = float(input("Enter score #5: "))
num_list.append(num)
num = float(input("Enter score #6: "))
num_list.append(num)
num = float(input("Enter score #7: "))
num_list.append(num)
#remove the lowest value
lowest = min(num_list)
num_list.remove(lowest)
total = sum(num_list)
length = len(num_list)
average = (total/length)
print()


print("---------Results------")
print("Lowest score",lowest)
print("Modified list: ",num_list)
print("Average: ", format(average,'.2f'))
print("-----------------------")
