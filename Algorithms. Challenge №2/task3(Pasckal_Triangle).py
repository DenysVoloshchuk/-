def calculate_pascal_row(row_number):
    row = [1]
    for i in range(1, row_number):
        next_value = row[-1] * (row_number - i) // i
        row.append(next_value)
    return row

def main():
    while True:
        try:
            row_number = int(input("Введіть номер рядка трикутника Паскаля: "))
            if row_number < 1:
                print("Номер рядка повинен бути більше або рівним 1.")
                return

            pascal_row = calculate_pascal_row(row_number)
            print(f"{row_number}-ий рядок трикутника Паскаля: {pascal_row}")
        except ValueError:
            print("Будь ласка, введіть ціле число.")

if __name__ == "__main__":
    main()
