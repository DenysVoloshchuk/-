def read_matrix():
    N = int(input("Введіть розмір матриці (N):"))
    entry_point = tuple(map(int, input("Введіть координати точки входу (розділені пробілом):").split()))
    print("Введіть матрицю поля (рядки розділені пробілом, символи між собою):")
    matrix = [input().split() for _ in range(N)]
    return N, entry_point, matrix

def get_next_direction(current_direction, obstacle):
    if obstacle == "\\":
        return (current_direction + 1) % 4
    elif obstacle == "/":
        return (current_direction - 1) % 4
    elif obstacle == "_":
        return (current_direction + 2) % 4
    elif obstacle == "|":
        return (current_direction + 2) % 4
    else:
        return current_direction

def get_next_position(current_position, current_direction):
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    return current_position[0] + moves[current_direction][0], current_position[1] + moves[current_direction][1]

def find_exit(N, entry_point, matrix):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # directions: right, down, left, up
    current_position = entry_point
    current_direction = 0  # initial direction: right

    while True:
        x, y = current_position
        if x < 0 or x >= N or y < 0 or y >= N:
            return current_position  # Exit found
        elif matrix[x][y] != ".":
            current_direction = get_next_direction(current_direction, matrix[x][y])
        current_position = get_next_position(current_position, current_direction)

def main():
    N, entry_point, matrix = read_matrix()
    exit_point = find_exit(N, entry_point, matrix)
    print("Координати точки виходу:", exit_point)

if __name__ == "__main__":
    main()
