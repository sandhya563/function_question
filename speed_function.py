# def driver_speed(speed):
#     count=0
#     if speed<=70:
#         print(speed,"ok")
#     elif speed>70:
#         value =speed-70
#         count= value/5
#         print(" driver points",int(count))
#         if count>12:
#             print(count,"license suspended")
# s=int(input("enter your speed"))
# driver_speed(s)

def driver_speed(speed):
    count=0
    if speed<=70:
        print(speed,"ok")
    elif speed>70:
        i=0
        value=speed-70
        while i<=value:
            if i%5==0:
                count=count+1
            i=i+1
        print(int(count))
        if count>12:
            print("license suspended")
speed=int(input("enter your speed"))
driver_speed(speed)

