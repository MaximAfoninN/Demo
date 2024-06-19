dict = {"Рома": 25, "Влад": 32}
age = dict["Влад"]
print(age)
print()

person = {
    "имя": "Максим",
    "возраст": "35",
    "пол": "Мужчина",
    "рост": "180",
    "вес": "80",
    "размер ноги": "44",
}

print(person["имя"])
print(person["возраст"])
print(person["пол"])
print(person["рост"])
print(person["вес"])
print(person["размер ноги"])
print()

person["размер ноги"] = 39
print(person["размер ноги"])
print(person)

del person["возраст"]
print(person)
