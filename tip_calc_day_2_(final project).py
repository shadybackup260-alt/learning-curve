print("welcome to tip calculator")
total_bill = float(input("what is the total bill? "))
tip_percent = int(input("what tip would you like to give? 10 12 15 "))
tip_percent /= 100
pepole_num = int(input("how many pepole to split the bill? "))
bill_with_tip = total_bill*tip_percent+total_bill
bill_per_person = bill_with_tip/pepole_num
final_payment =round(bill_per_person , 2)
print(f"every person should pay {final_payment}")
