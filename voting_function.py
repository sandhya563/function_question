def eligiable_for_vote(age):
    if age<18:
        print(age,"your not eligible")
    elif age==18 or age>18:
        print(age,"your eligible")
    else:
        print(age,"your not eligible")
eligiable_for_vote(40)