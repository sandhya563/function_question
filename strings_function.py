def strings(hello,welcome):
    if len(hello)>len(welcome):
        print("welcome")
    elif len(hello)==len(welcome):
        print(hello)
        print(welcome)
hello=input("enter your name")
welcome=input("enter your name2")
strings(hello,welcome)