red_amount= int(input())
green_amount= int(input())
blue_amount= int(input())

min_val = red_amount
if green_amount < min_val:
    min_val = green_amount
if blue_amount < min_val:
    min_val = blue_amount
# remove gray
red_amount = red_amount - min_val
green_amount = green_amount - min_val
blue_amount = blue_amount - min_val

print(red_amount, green_amount, blue_amount)