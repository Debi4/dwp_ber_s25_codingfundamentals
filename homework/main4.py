scores = [15, 19, 17, 12, 17, 13]
print(scores[0])
print(scores[5])
print(max(scores))
print(min(scores))
scores.append(21)
print(scores)
scores.sort()
print(scores)
scores.remove(17)
print(scores)
scores.pop(3)
print(scores)
print(len(scores))

groceries = {'tomatoes', 'milk', 'carrots', 'tomatoes'}
print(groceries)
print()
print( "--------------" )
def area_of_home(meters):
    centimeter = 100
    size = centimeter * meters
    return size

bathroom = 4
kitchen = 2
bedroom = 10

Bathroom_size = area_of_home(bathroom)
Kitchen_size = area_of_home(kitchen)
Bedroom_size = area_of_home(bedroom)
print("Bathroom length:", Bathroom_size, "cm")
print("Kitchen length:", Kitchen_size, "cm")
print("Berdoom length:", Bedroom_size, "cm")