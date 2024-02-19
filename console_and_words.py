import re
from collections import Counter

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        words = re.findall(r'\b[а-яА-Яa-zA-Z]+\b', text.lower())  # Вибір кириличних слів з тексту
        return Counter(words)

def main():
    file_path = input("Введіть шлях до файлу: ")
    try:
        word_count = process_file(file_path)
        sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
        for word, count in sorted_word_count:
            print(f"{word}: {count}")
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")

if __name__ == "__main__":
    main()
