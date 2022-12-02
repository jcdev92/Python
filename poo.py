from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def say_hello(self):
        pass

    @abstractmethod
    def say_goodbye(self):
        pass

    def __str__(self):
        return f'{self.name} is {self.age} years old.'


class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school
        self.__is__enabled = True

    def say_hello(self):
        return f'Hello, I am {self.name} and I am a student at {self.school}.'

    def say_goodbye(self):
        return f'Goodbye, I am {self.name} and I am a student at {self.school}.'

    def enable(self):
        self.__is__enabled = True

    def disable(self):
        self.__is__enabled = False

    def is_enabled(self):
        return self.__is__enabled

    def __str__(self):
        return f'{super().__str__()} I am a student at {self.school}.'


def main():
    student = Student('John', 18, 'MIT')
    print(student)
    print(student.say_hello())
    print(student.say_goodbye())
    student.enable()
    print(student.is_enabled())


if __name__ == '__main__':
    main()
