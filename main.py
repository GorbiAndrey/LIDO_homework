class Stack:
    def __init__(self):
        self.list = []

    def isEmpty(self):
        return self.list == []

    def push(self, item):
        self.list.append(item)

    def pop(self):
        return self.list.pop()

    def peek(self):
        return self.list[len(self.list) - 1]

    def size(self):
        return len(self.list)


def balanceCheck(symbolString):
    s = Stack()
    balanced = True
    i = 0

    while i < len(symbolString) and balanced:
        symbol = symbolString[i]
        if symbol == "(" or symbol == "{" or symbol == "[":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                last_symbol = s.peek()
                if last_symbol == "(" and symbol == ")":
                    s.pop()
                elif last_symbol == "[" and symbol == "]":
                    s.pop()
                elif last_symbol == "{" and symbol == "}":
                    s.pop()
                else:
                    balanced = False

        i += 1

    if balanced and s.isEmpty():
        return ('Сбалансированно')
    else:
        return ('Не сбалансированно')


print(balanceCheck('(((([{}]))))'))
print(balanceCheck('[([])((([[[]]])))]{()}'))
print(balanceCheck('{{[()]}}'))
print(balanceCheck('}{}'))
print(balanceCheck('{{[(])]}}'))
print(balanceCheck('[[{())}]'))