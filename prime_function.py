def check_prime(num):
    i=2
    while i<num:
        if num%i==0:
            print(num,"not prime")
            break
        else:
            print(num,"prime")
            break
        i=i+1
check_prime(18)