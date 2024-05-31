def main(input_str: str) -> str:
    try:
        a, op, b = input_str.split()
        a = int(a)
        b = int(b)

        if a < 1 or a > 10 or b < 1 or b > 10:
            raise ValueError("Цифры должны быть между 1 и 10")

        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            result = a // b
        else:
            raise ValueError("Неправильная арифмитическая операция.")

        return str(result)
    except Exception as e:
        return "Error: " + str(e)

if __name__ == "__main__":
    input_expression = input("Введите арифмитическую операция (e.g., '2 + 3'): ")
    result = main(input_expression)
    print("Result:", result)


