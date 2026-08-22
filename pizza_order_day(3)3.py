print("welcome to pizza deliveries!")
size = input("what size do you want S, M, L")
add_pepperoni = input("do you want pepperobi? Y or N")
extra_cheese = input("do you want extra cheese? Y or N")
bill = 0
if size =="S":
    bill=15
    print("you chose a small pizza which is $15")
elif size =="M":
    bill =20
    print("you chose a medium pizza which is $20")
else:
    bill =25
    print("you chose a large pizza which is $25")

if add_pepperoni =="Y":
        if size =="S":
            bill+=2
        else:
            bill+=3
if extra_cheese =="Y":
     bill+=1
print(f"your order will be {bill}")
