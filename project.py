name = input("hello customer what is your name?")
print("welcome "+name)


quiz = input(name+" type menu to access our accessories")
menu = ("fried chips, chicken chips, soda")

if quiz == "menu":
    print(menu)

while quiz != "menu":
    print("please follow the above instructions and try again")
    quiz = input(name + " type menu to access our accessories")
    if quiz == "menu":
        print(menu)

sw = input("what would you like to have")







