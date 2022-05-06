current_price = int(input())
last_months_price = int(input())
change = current_price - last_months_price
mortgage = current_price * 0.051 / 12
print('This house is $', end='')
print(current_price, end='. ')
print('The change is $', end='')
print(change, end=' ')
print('since last month.')
print('The estimated monthly mortgage is $', end='')
print(f'{mortgage:.2f}.')
   