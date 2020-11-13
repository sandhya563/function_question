def expenses_of_student(num_student,budget):
    value=num_student*budget
    print(value)
    if value<=50000:
        print("budget is under controll")
    else:
        print("budget is under controll")
num_student=int(input("enter students number"))
budget=int(input("enter expenses of a student"))
expenses_of_student(num_student,budget)
