def multiple(limit):
    i=1
    sum=0
    while i<=limit:
        if i%3==0 or i%5==0:
            sum=sum+i 
            print("multiples of 3 or 5:-",i)
        i=i+1
    print("sum of 3 and 5:-",sum)
limit=int(input("enter your num"))
multiple(limit)
