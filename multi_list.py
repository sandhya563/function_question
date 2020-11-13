list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
a=[]
i=0
while i < len (list1):
    b=(list1[i]*list2[i])
    a.append(b)
    i=i+1
print(a)