class People:
    def __init__(self, people_list=None):
        if people_list is None:
            people_list = []
        self._people = people_list

    def add_people(self, name):
        self._people.append(name)

    def __iter__(self):
        return iter(self._people)


people = People(["Михаил", "Артем", "Николай", "Владимир"])
people.add_people("Ольга")

for person in people:
    print(person)
