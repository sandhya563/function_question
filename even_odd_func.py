def show_numbers(num1):
    i=0
    while i<=num1:
        if i%2==0:
            print("even",i)
        else:
            print("odds",i)
        i=i+1
num1=int(input("enter your num1"))
show_numbers(num1)