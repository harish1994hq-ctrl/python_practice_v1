def numbers(lower,upper):
    for i in range(lower,upper + 1):
        if(i%2!=0):
            print("the odd numbers is ", i)
    print("**********************************")
    for j in range (lower, upper+1):
        if (j%2==0):
            print("The even number is : ",j)

numbers(1,10)