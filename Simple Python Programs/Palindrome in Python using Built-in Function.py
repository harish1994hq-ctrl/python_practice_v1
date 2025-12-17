def is_palindrom(n):
    return str(n) == ''.join(reversed(str(n)))

n = int(input('Enter the number: '))

if is_palindrom(n):
    print("The number is a palindrom!")
else:
    print("The number is not a palindrom.")