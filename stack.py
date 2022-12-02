from dataclasses import dataclass


# push, pop, top, bottom, is:empty
@dataclass
class Stack:
    __elements = []

    def get_elements(self):
        return self.__elements

    def push(self, element):
        self.__elements.append(element)

    def pop(self):
        return self.__elements.pop()

    def top(self):
        return self.__elements[-1]

    def bottom(self):
        return self.__elements[0]

    def is_empty(self):
        return len(self.__elements) == 0

    def __str__(self):
        return str(self.__elements)


if __name__ == '__main__':
    stack = Stack()

print(stack.is_empty())
stack.push(1)
stack.push(2)
stack.push(3)

print(stack)
print(stack.pop())
print(stack)
print(stack.top())
print(stack.bottom())
print(stack.is_empty())
print(stack.get_elements())
