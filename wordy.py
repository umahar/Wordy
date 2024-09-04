def answer(question):
    result = 0
    que = question
    que_list = question[0:-1].split()
    equation = []
    check_1 = "what" not in que.lower()

    if check_1:
        raise ValueError("unknown operation")
    for word in que_list:
        if word.startswith("-"):
            equation.append(word)
        if word.isdigit():
            equation.append(word)
        if "plus" in word:
            equation.append("+")
        if "minus" in word:
            equation.append("-")
        if "multiplied" in word:
            equation.append("*")
        if "divided" in word:
            equation.append("/")
    if len(equation) == 1:
        if "cubed" in que_list:
            raise ValueError("unknown operation")
        return int(equation[0])
    elements_to_check = ["+", "-", "*", "/"]
    any_in_list = any(element in equation for element in elements_to_check)
    if not any_in_list:
        if "cubed" in que_list:
            raise ValueError("unknown operation")
        raise ValueError("syntax error")

    if equation[1].isdigit():
        raise ValueError("syntax error")
    if len(equation) == 3:
        if equation[1] == "-":
            result = minus(equation[0], equation[2])
            return result
        if equation[1] == "*":
            result = multiply(equation[0], equation[2])
            return result
        if equation[1] == "+":
            result = plus(equation[0], equation[2])
            return result
        if equation[1] == "/":
            result = divide(equation[0], equation[2])
            return result
    if len(equation) % 2 == 0:
        raise ValueError("syntax error")
    if equation[1] == "-":
        result = minus(equation[0], equation[2])
        if equation[3] == "-":
            result = minus(result, equation[4])
            return result
        if equation[3] == "+":
            result = plus(result, equation[4])
            return result
        if equation[3] == "/":
            result = divide(result, equation[4])
            return result
        if equation[3] == "*":
            result = multiply(result, equation[4])
            return result
    if equation[1] == "+":
        result = plus(equation[0], equation[2])
        if equation[3] == "-":
            result = minus(result, equation[4])
            return result
        if equation[3] == "+":
            result = plus(result, equation[4])
            return result
        if equation[3] == "/":
            result = divide(result, equation[4])
            return result
        if equation[3] == "*":
            result = multiply(result, equation[4])
            return result
    if equation[1] == "*":
        result = multiply(equation[0], equation[2])
        if equation[3] == "-":
            result = minus(result, equation[4])
            return result
        if equation[3] == "+":
            result = plus(result, equation[4])
            return result
        if equation[3] == "/":
            result = divide(result, equation[4])
            return result
        if equation[3] == "*":
            result = multiply(result, equation[4])
            return result
    if equation[1] == "/":
        result = divide(equation[0], equation[2])
        if equation[3] == "-":
            result = minus(result, equation[4])
            return result
        if equation[3] == "+":
            result = plus(result, equation[4])
            return result
        if equation[3] == "/":
            result = divide(result, equation[4])
            return result
        if equation[3] == "*":
            result = multiply(result, equation[4])
            return result


def plus(num1, num2):
    return int(num1) + int(num2)


def minus(num1, num2):
    return int(num1) - int(num2)


def multiply(num1, num2):
    return int(num1) * int(num2)


def divide(num1, num2):
    return int(num1) / int(num2)


print(answer("What is 5?"))
