class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мне {self.age} лет, я живу в {self.city}.")

    def is_adult(self):
        return self.age >= 18

    def __str__(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Город: {self.city}"

# Создание экземпляров класса Person
person1 = Person("Иван", 25, "Москва")
person2 = Person("Аня", 16, "Санкт-Петербург")


person1.introduce()
person2.introduce()


print(person1.is_adult())
print(person2.is_adult())


print(person1)
print(person2)
