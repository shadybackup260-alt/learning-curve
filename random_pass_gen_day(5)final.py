import random
letters =["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
"k", "l", "m", "n", "o", "p", "q", "r", "s", "t", 
"u", "v", "w", "x", "y", "z" "A", "B", "C", "D"
, "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
 "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numbers=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_",
"=", "+", "[", "]", "{", "}", "|",
 ";", ":", "'",".", "<", ">", "/", "?", "~", "`"]

print("welcome to the pypassword generator!")
nr_letters=int(input("how many letters would you like in your password"))
nr_numbers=int(input("how many numbers would you like in your password"))
nr_symbols=int(input("how many synbols would you like in your password"))

password=""
for char in range(1 , nr_letters + 1):
    password += random.choice(letters)

for num in range(1, nr_numbers + 1):
    password += random.choice(numbers)

for symb in range(1, nr_symbols + 1):
    password += random.choice(symbols)
my_pass = password.split("")
# هنا بيحول الـ string لـ list (قائمة) من الحروف، يعني كل حرف يبقى عنصر لوحده.
random.shuffle(my_pass)
# دي الدالة اللي بتخلط عناصر الـ list بشكل عشوائي (زي ما تخلط ورق كوتشينة). بقى بتغير في chars نفسها مباشرة (in-place)، يعني مش بترجع قيمة جديدة، هي بتعدل على الأصل.
randomized_password = ''.join(my_pass)

# هنا بيرجع يجمع الحروف اللي في الـ list ويحولها تاني لـ string واحد متصل.

# ''.join(chars) معناها: خد كل عناصر الـ list وحطهم مع بعض في string واحد، والفاصل بينهم هو '' (يعني مفيش فاصل، الحروف هتتلزق في بعض على طول).

print(randomized_password)

# https://claude.ai/chat/9f6c9224-9c41-49d8-9ba5-e57c5d0661f1
# for understanding the concept
