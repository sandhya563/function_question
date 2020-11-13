def perfect_number(input):
    a=1
    sum=0
    while a <input:
        if input%a==0:
            sum=sum+a 
        a+=1
    if sum==input:
        print("perfect number")     
    else:
        print("not a perfect number") 
input=int(input("enter the num"))
perfect_number(input) 