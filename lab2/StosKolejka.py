# Zadanie 1
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


# Zadanie 2,3
def checkBraccets(inputString):
    # Tworzenie słownika dla par nawiasów
    slownik = {"}": "{", ")": "(", "]": "["}
    stos = Stack()
    index = 0
    error = True
    while (index < len(inputString)) and error:
        symbol = inputString[index]
        # Jeśli znak to otwierający nawias, dodajemy go do stosu
        if symbol == "(" or symbol == "{" or symbol == "[":
            stos.push(symbol)
        else:
            # Jeśli znak to zamykający nawias
            # Sprawdzamy, czy stos jest pusty
            if stos.isEmpty():
                error = False
            # Sprawdzamy, czy znak zamykający odpowiada otwierającemu nawiasowi na szczycie stosu
            elif slownik.get(symbol) == stos.peek():
                # Jeśli tak, usuwamy otwierający nawias ze stosu
                stos.pop()
        index += 1
    # Sprawdzamy, czy wszystkie nawiasy zostały zamknięte i czy stos jest pusty
    if error and stos.isEmpty():
        return True
    else:
        return False


print(checkBraccets("(()()()())"))  # true
print(checkBraccets("((((((())"))  # false
print(checkBraccets("{()()([])()()}"))  # true
print(checkBraccets("{()([)]()[[](])}()}"))  # false


def onp(expression):
    operators = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: x / y,
                 '^': lambda x, y: x ** y}
    stack = Stack()
    for symbol in expression.split():
        if symbol.isdigit():
            stack.push(float(symbol))
        elif symbol in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operators[symbol](operand1, operand2)
            stack.push(result)
        elif symbol == '=' and stack.size() == 1:
            return stack.peek()
    return "Coś poszło nie tak"


wyrazenie = "7 3 + 5 2 - 2 ^ * ="
wynik = onp(wyrazenie)
print("Wynik wyrażenia", wyrazenie, "to:", wynik)
