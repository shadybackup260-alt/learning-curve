twohundred= int(input("how many 200 you have?"))*200
onehundred= int(input("how many 100 you have?"))*100
fifty= int(input("how many 50 you have?"))*50
twenty= int(input("how many 20 you have?"))*20
ten= int(input("how many 10 you have?"))*10
five=int(input("how many 5 you have?"))*5
total = twohundred + onehundred + fifty + twenty + ten + five

shifts = int(input("how many shifts was there before you"))
if shifts ==1:
    tasleem = int(input("how much did the shift before you make?"))
    masrofat = int(input("how much was the masrofat"))

    final_tasleem = total - tasleem
    dakhl = final_tasleem + masrofat
    print(f"the total money you have is {total} ,your tasleem is {final_tasleem}, your masrofat is {masrofat}, your dakhl is {dakhl}")
else: 
    tasleem_1 = int(input("how much did the first shift make?"))
    masrofat_1 = int(input("how much masrofat did the first shift make?"))
    dakhl_1 = int(input("houw much dakhl did the first shift make?"))

    tasleem_2 = int(input("how much did the secound shift make?"))
    masrofat_2 = int(input("how much masrofat did the secound shift make?"))
    dakhl_2 = int(input("houw much dakhl did the secound shift make?"))

    masrofat = int(input("how much was your masrofat"))

    final_tasleem = total - (tasleem_1 +tasleem_2)
    dakhl = final_tasleem + masrofat
    safi_tasleem = tasleem_1 + tasleem_2 + final_tasleem
    safi_masrofat = masrofat + masrofat_1 + masrofat_2
    safi_dakhl = dakhl + dakhl_1 + dakhl_2
    print(f"the total money you have is {total} ,your tasleem is {final_tasleem}, your masrofat is {masrofat}, your dakhl is {dakhl},\n your safi tasleem is{safi_tasleem}, your safi masrofat is {safi_masrofat}, your safi dakhl is {safi_dakhl}")
