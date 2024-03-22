x = 5
y = 5
s = "python "
q = "is "
r = "awesome"
print(s+q+r)
age = 70
if age >= 18:
    print("you are adult")


president_age = 30
nationality = "nigerian"
if president_age >= 18 and nationality == "kenyan":
    print("you are not eligible for president")

elif president_age <= 18 and nationality == "nigerian":
    print("you are not eligible for president")

else:
    print("you are eligible for president")

#concatinate i.e attaching strings together
first_name = "nivel  "
second_name = "wainaina"
full_name = (first_name+second_name)
print(full_name)


#casting i.e attaching an integer with a string(integer to string)
first_name = "nivel"
second_name = 9
full_name = first_name+" "+str(second_name)
print(full_name)

#casting string to integer
first_name = 8
second_name = "50"
full_name = int(second_name)+first_name
print(full_name)

#string to float
first_name = 8.6
second_name = "50.0"
full_name = first_name+float(second_name)
print(full_name)

# looping (while)
student_name = input("enter you name:")
while student_name == "":
    print("name not entered")
    student_name = input("enter your name:")
print("hello" + student_name)

# if elif and else
name = input("enter your name:")
if name == "ben":
    evil_type = input("enter your evil type")
    if evil_type == "yes":
        print("get away evil ben")
    else:
        print("welcome good ben")
        exit()
    print("you are not allowed here ben get away!!!")
else:
    print("welcome" +name+ "to our coffee shop")




#for loop
estates = ["karen", "kileleshwa", "benjamina", "stannia"]
for x in estates:
    print(x)

#list using square brackets
estates = ["karen", "kileleshwa", "benjamina", "stannia"]
print(estates)

#range function
for x in range(5):
    print("nigel")

#while loop
x = 1
while x <= 5:
    print("python")
    x += 1
else:
    print("finished")



#nested loops
adj = ["big", "tasty", "yummy"]
fruit = ["apple", "banana", "cherry"]
for x in adj:
    print(x)
    for y in fruit:
        print(y)




name = [input("first_name:"), input("second_name:"), input("last_name:")]
space = [input(""), input(""), input("")]
for x in name:
    print(x)
    for y in space:
        print(y)






