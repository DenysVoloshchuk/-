import math

def calculate_angle(x, y):
    return math.degrees(math.atan2(y, x))

def main():
    x1 = float(input("Введіть координату x1: "))
    y1 = float(input("Введіть координату y1: "))
    x2 = float(input("Введіть координату x2: "))
    y2 = float(input("Введіть координату y2: "))

    angle_a = calculate_angle(x1, y1)
    angle_b = calculate_angle(x2, y2)

    if angle_a > angle_b:
        print("Відрізок OA утворює більший кут з віссю OX.")
    elif angle_b > angle_a:
        print("Відрізок OB утворює більший кут з віссю OX.")
    else:
        print("Відрізки OA і OB утворюють однаковий кут з віссю OX.")

if __name__ == "__main__":
    main()
