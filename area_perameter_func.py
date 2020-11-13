def area(length,width):
    formula = length*width
    print(formula)
area(12,7)

def parameter(**length,num,width,num2):
    formula = length+num+width+num2
    return formula
parameter(a=12,b=12,c=7,d=7)