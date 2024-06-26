# The sum of squares of numbers from 1 to 10.
sum = 0
for i in range(1,11):
    print(f"{i} square = {i**2}")
    sum = sum + i**2
print()
print(f"The sum of squares of numbers from 1 to 10 : {sum}")
