def merge_arrays(*arrays):
    merged_array = []
    for array in arrays:
        merged_array.extend(array)

    # Видалення дублікатів та фільтрація чисел, які кратні 5
    merged_array = sorted(set(merged_array))
    merged_array = [num for num in merged_array if num % 5 != 0]

    return merged_array

def main():
    arrays = []
    while True:
        array = input("Введіть через кому числа для масиву (Enter щоб завершити): ").strip()
        if array:
            try:
                array = [int(num) for num in array.split(',')]
                arrays.append(array)
            except ValueError:
                print("Будь ласка, введіть цілі числа.")
        else:
            break

    if arrays:
        merged_array = merge_arrays(*arrays)
        print("Результат об'єднання масивів:", merged_array)
    else:
        print("Не введено жодного масиву.")

if __name__ == "__main__":
    main()
