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


#looping i.e repeating
i = 1
while i < 7:
    print(i)
    i += 1



#looping
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
        print("the answer is" ,i)




