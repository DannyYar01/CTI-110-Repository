# I was supposed to put a comment here
# Danny Yarborough

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
##    A_score = 90
##    B_score = 80-89
##    C_score = 79-70
##    D_score = 69-60
##    F_score = 59
    
    score = int(input("Enter your grade here: "))

    if score >= 89:
        print('Your grade is: A')
    elif score >= 80:
        print('Your grade is: B')
    elif score >= 70:
        print('Your grade is: C')
    elif score >= 60:
        print('Your grade is: D')
    else:
        print("Your grade is: F")

    







# program start
main()
