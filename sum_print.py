# #part 1
# def add_numbers(num1,num2):
#     return(num1+num2)
# print(add_numbers(56,12))

# part 2
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
f=[]
def add_numbers(a,b):
    i=0
    while i < len(a):
        c=(a[i]+b[i])
        f.append(c)
        i+=1
    return(f)
print(add_numbers(list1,list2))