# Создать сотрудника Mary, пользуясь классом
# Employee и перенести его в другую программу,
# используя модуль Pickle и файловую систему.
# Узнать про + и - модуля Pickle.


# первая часть ДЗ, вторая часть в файле hw14_2.py
# результат в файле result1.png
import pickle


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def set_salary(self, salary):
        self.salary = salary

    def __repr__(self):
        return f"Employ {self.name} is {self.age} old and has {self.salary} salary."


if __name__ == "__main__":
    mary = Employee("Mary", 25, 10000)
    print(mary)
    mary.set_salary(14000)
    print(mary)

    with open('data.pickle', 'wb') as f:
        pickle.dump(mary, f)
