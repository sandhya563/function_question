def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)
num=int(input("enter your num"))
fact = factorial(num)
print(fact)