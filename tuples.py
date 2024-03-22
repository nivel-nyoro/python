#tuples are unchangable unlike lists
#must change from tuple to lists
classes = ("safari", "brave", "sos", "emobilis", "counter")
print(classes)
new_classes = list(classes)
new_classes.append("pine")
print(new_classes)
new_classes[1] = "east"
classes = tuple(new_classes)
print(classes)







