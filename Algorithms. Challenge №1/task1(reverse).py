def reverse_text_file(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            text = input_file.read()
            reversed_text = text[::-1]  # Зворотнє перетворення тексту

        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(reversed_text)
        print("Файл успішно збережено.")
    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")

def main():
    while True:
        input_file_path = input("Введіть шлях до вхідного файлу: ")
        output_file_path = input("Введіть шлях до вихідного файлу: ")
        reverse_text_file(input_file_path, output_file_path)

if __name__ == "__main__":
    main()
