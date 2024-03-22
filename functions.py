

untensils = {"plate", "cup", "fork", "spoon"}
dishes = {"spoon", "sinia", "mug", "bowl"}
print(dishes.intersection(untensils))


dishes = ("ugali", "chicken", "chips", "hotdog")
x = ("chapaiifahm",)
dishes += x
print(dishes)



#1
def largest_number():
    x = [1,2,3,4,5,6,7,8,9,10]
    return max(x)
print(largest_number())

#2
def my_function(*number):
    print(max(number))
my_function(1,6,60)





name = ["nivel", "dababy", "lil baby", "lildark"]
marks = ["100", "80", "60", "10"]
grade = zip(name,marks)
print(dict(grade))



#adding items in a set
laps = {"plate", "cup", "fork", "spoon"}
laps.add("kake")
print(laps)


#adding another set
countries = {"kenya", "france", "germany", "uganda"}
countries.update({"ethiopia", "madagascar"})
print(countries)



fruits = ["apple", "banana", "cherry", "berry", "orange", "apple", "banana"]
repeated = []
for x in fruits:
    if fruits.count(x)>1:
        repeated.append(x)
        if x not in repeated:
            repeated.append(x)
print(repeated)




