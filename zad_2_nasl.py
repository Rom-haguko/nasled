class Bachelor:
    def __init__(self, firstName, lastName, group, averageMark):
        self.firstName = firstName
        self.lastName = lastName
        self.group = group
        self.averageMark = averageMark

    def getScholarship(self):
        if self.averageMark==5:
            return 10000
        elif self.averageMark > 3:
            return 5000
        return 0

class Undergraduate(Bachelor):
    def getScholarship(self):
        if self.averageMark==5:
            return 15000
        elif self.averageMark > 3:
            return 7500
        return 0

students = [
    Bachelor("Иван", "Иванов", "Группа A", 5),
    Bachelor("Пётр", "Петров", "Группа B", 4),
    Bachelor("Андрей", "Сидоров", "Группа C", 3),
    Undergraduate("Алексей", "Смирнов", "Группа D", 5),
    Undergraduate("Мария", "Кузнецова", "Группа E", 4),
    Undergraduate("София", "Белова", "Группа F", 2),
]

for i in students:
    print(f'{i.firstName} {i.lastName} ({i.group}) получает стипендию: {i.getScholarship()}')