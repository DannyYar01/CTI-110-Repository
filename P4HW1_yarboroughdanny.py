#Cti- 110
#P4hw1 - score list
# Danny Yarborough
# 3/25/2022

def main():
    total = 0
    grade_list = []


    num = int(input("Enter number of scores to total: "))
    for i in range (0, num):
        grade = int(input("Enter score #" + str(i + 1)+ ": "))
        while grade < 0 or grade > 100:
            print("INVALID score entered:")
            print("Score should be between 0 and 100")
            grade = int(input("Enter score #" + str(i + 1)+ ": "))
        grade_list.append(grade)

    lowest = min(grade_list)
    grade_list.remove(lowest)
    print(lowest)
    print(grade_list)
    average = sum(grade_list)/ (num - 1)
    print(average)
    if average > 89:
        grade = "A"
    elif average > 79:
        grade = "B"
    elif average > 69:
        grade = "C"
    elif average > 59:
        grade = "D"
    else:
        grade = "F"
    print(grade)

main()
