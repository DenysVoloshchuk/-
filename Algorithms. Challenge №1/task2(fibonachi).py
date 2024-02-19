def fibonacci(index):
    if index <= 0:
        return "Індекс повинен бути більше 0"
    elif index == 1:
        return 0
    elif index == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(index - 2):
            a, b = b, a + b
        return b

def main():
    try:
        index = int(input("Введіть індекс числа Фібоначчі: "))
        result = fibonacci(index)
        print(f"Число Фібоначчі з індексом {index}: {result}")
    except ValueError:
        print("Будь ласка, введіть ціле число.")
    except Exception as e:
        print(f"Виникла помилка: {e}")

if __name__ == "__main__":
    main()
5