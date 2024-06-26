# The function y=x^2 from 1 to 10 in increments of 0.5.
print("The function y=x^2 from 1 to 10 in increments of 0.5 : ")
print()
i = 0.5
for x in range(2,21):
    i = i + 0.5
    print(f"y = {i}  x = {i**2}")


# The factorials of numbers from 1 to 5 (inclusive).
print("The factorials of numbers from 1 to 5 (inclusive):")
print()
f = 1
for i in range(1,6):
    f = i * f
    print(f"Factorial of {i} = {f}")

