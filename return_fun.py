def create_adder(x,y):  
    def adder(z):
        sum=x+y
        return sum+z
    return adder  
add_15 = create_adder(15,10)  
print(add_15(10))