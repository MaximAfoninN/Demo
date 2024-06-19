my_list = [1, 2, 3, 4, 5]
print(my_list)
print(my_list[0], my_list[2])
print(my_list[:1], my_list[2:3])
print(my_list[:3])
print()

city_list = ["Ростов", "+", "на", "-", "Дону"]
print(city_list)
city_list.insert(1, "-")
city_list.pop(2)
print(city_list)
print(city_list[0], city_list[1], city_list[2], city_list[3], city_list[4])
print()

unsorted_list = ["a", "s", "1", "a", "32", "23"]
print(unsorted_list)
print()
letter_list = unsorted_list.copy()
letter_list.pop(2)
letter_list.pop(4)
letter_list.pop(3)
print(letter_list)
print()
number_list = unsorted_list.copy()
number_list.pop(0)
number_list.pop(0)
number_list.pop(1)
print(number_list)
print()

letter_list.pop()
letter_list.reverse()
print(letter_list)
print()

print(unsorted_list)
my_set = set(unsorted_list)
print(my_set)
