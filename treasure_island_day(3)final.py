print(''' ,-----------------------------.----------------------------------.
|                             |                                  |
|    .    .    ,---------     |     ------------------------.    |
|    |    |    |              |                             |    |
|    |    `----"--------------'    ,-------------------.    |    |
|    |                             |                   |    |    |
|    :--------------.--------------"----     ,---------:    |    |
|    |              |                        |         |    |    |
|    :---------     |    .    ,---------.    |    .    |    `----:
|    |              |    |    |         |    |    |    |         |
|    |     ---------'    |    :----     |    |    |    |    .    |
|    |                   |    |         |    |    |    |    |    |
|    `-------------------'    |     ----'    |    |    |    |    |
|                             |              |    |    |    |    |
:--------------.---------.    :--------------'    |    :----'    |
|              |         |    |                   |    |         |
|    .    .    |    .    |    |    ,--------------:    `----     |
|    |    |    |    |    |    |    |              |              |
|    |    |    "    |    |    |    |     ---------"---------.    |
|    |    |         |    |    |    |                        |    |
|    |    `---------"----'    |    |    ,---------.    .    |    |
|    |                        |    |    |         |    |    |    |
|    :---------.--------------:    |    |    .    |    |    |    |
|    |         | X            |    |    |    |    |    |    |    |
|    "    .    `---------     |    |    `----'    |    `----'    |
|         |                   |    |              |              |
`---------"-------------------'    `--------------"--------------' ''')
print("welcome to trasure island!")
print("your misson id to find the treasure")
lr = input("you have 2 ways right or left, what will you choose, L or R")
if lr == "L":
    sw =input("you can either swim or wait, what will you choose, S or W")
    if sw =="W":
        door= input("you have 3 doors, red yellow and blue, which will you choose R Y B")
        if door =="R":
            print("Burned by fire. Game Over.")
        elif door == "B":
                print("Eaten by beasts. Game Over.")
        elif door == "Y":
                print("you found the treasure, YOU WIN!")
        else:
            print("game over.")
    else:
        print("you got Attacked by trout. Game Over.")

else:
    print("you fell in a hole! game over.")
