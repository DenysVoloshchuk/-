def read_time(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

def main():
    wake_up_time = read_time(input("Введіть час, коли підліток проснувся (hh:mm): "))
    N = int(input("Введіть кількість подій: "))

    events = []
    for i in range(N):
        print(f"Введіть інформацію про {i+1}-у подію (початковий час, кінцевий час, час на дорогу, кількість учасників), розділені пробілом:")
        start_time, end_time, travel_time, participants = input().split()
        start_time = read_time(start_time)
        end_time = read_time(end_time)
        travel_time = int(travel_time)
        participants = int(participants)
        events.append((start_time, end_time, travel_time, participants))

    events.sort(key=lambda x: x[0])  # Сортуємо події за часом початку

    total_participants = 0
    current_time = wake_up_time
    for event in events:
        start_time, end_time, travel_time, participants = event
        if current_time + travel_time <= start_time:  # Перевіряємо, чи можна відвідати подію
            total_participants += participants
            current_time = start_time + (end_time - start_time) // 2  # Переміщаємося в середину події
        elif current_time >= start_time and current_time < end_time:  # Якщо вже на події
            time_spent = min(current_time + travel_time, end_time) - current_time
            proportion = time_spent / (end_time - start_time)
            total_participants += participants * proportion

    print("Максимальна кількість людей, яких може зустріти підліток:", int(total_participants))

if __name__ == "__main__":
    main()
