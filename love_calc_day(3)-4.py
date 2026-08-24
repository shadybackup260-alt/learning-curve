name1= input("enter your name")
name2 = input("enter her name")
name3 = name1 + name2

t= name3.count("t")
r= name3.count("r")
u= name3.count("u")
e= name3.count("e")
true = t+r+u+e
l= name3.count("l")
o= name3.count("o")
v =name3.count("v")
e= name3.count("e")
love = l+o+v+e
final_score =str(true)+str(love)
int_final_score =int(final_score)
if int_final_score<10 or int_final_score>90:
        print(f"your score is {int_final_score}% , you go together like coke and mentos")
elif int_final_score>=40 and int_final_score<=50:
        print(f"your score is {int_final_score}% , you are alright together")
else:
        print(f"your score is {int_final_score}% ")
