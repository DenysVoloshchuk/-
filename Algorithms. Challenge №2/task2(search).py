import re

def count_word_occurrences(word, mode, file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            occurrences = 0
            if mode == 1:
                occurrences = len(re.findall(re.escape(word), text, re.IGNORECASE))
            elif mode == 2:
                occurrences = len(re.findall(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE))
            print(f"Слово '{word}' згадується у тексті {occurrences} разів.")
    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")

def main():
    while True:
        word = input("Введіть слово(-0- - завершення роботи): ")
        if word == '-0-':
            break
        mode = int(input("Введіть режим роботи (1 - часткові співпадіння, 2 - точні співпадіння): "))
        file_path = input("Введіть шлях до текстового файлу: ")
        count_word_occurrences(word, mode, file_path)

if __name__ == "__main__":
    main()
