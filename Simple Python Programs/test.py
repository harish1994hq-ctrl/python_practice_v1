start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

print("Palindrome numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    temp = num
    rev = 0
    while temp > 0:
        dig = temp % 10
        rev = rev * 10 + dig
        temp = temp // 10
    if num == rev:
        print(num)
