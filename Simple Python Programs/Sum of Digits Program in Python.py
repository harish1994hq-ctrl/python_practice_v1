n =int(input('Enter a Number: '))

total = 0

while(n > 0):
    digit=n%10
    total=total+digit
    n=n//10
print('The total sum of digit is:',total)
