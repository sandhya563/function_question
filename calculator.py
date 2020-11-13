# # question no 6 ka part one
# def my_fun(x,y,sign):
#   if sign=="+":
#     return (x+y)
#   elif sign=="-":
#     return (x-y)
#   elif sign=="*":
#     return (x*y)
#   elif sign=="/":
#     return (x/y)
# x=int(input("no=="))
# y=int(input("2 no=="))
# sign=input("enter the sign")
# print(my_fun(x,y,sign))


def list_change(list1,list2):
    i=0
    list=[]
    while i < len(list1):
        stor=my_fun(list1[i],list2[i],sign)
        list.append (stor)
        i=i+1
    return list
print(list_change([5, 10, 50, 20],[2, 20, 3, 5]))
