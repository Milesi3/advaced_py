import random

__all__ = ['is_valid', 'generate_valid_arrangements']

def is_valid(arrangement):
    for i in range(len(arrangement)):
        for j in range(i + 1, len(arrangement)):
            if arrangement[i][0] == arrangement[j][0] or arrangement[i][1] == arrangement[j][1]:
                return False
            if abs(arrangement[i][0] - arrangement[j][0]) == abs(arrangement[i][1] - arrangement[j][1]):
                return False
    return True

def generate_random_arrangement():
    queens = [(i, random.randint(1, 8)) for i in range(1, 9)]
    return queens

def generate_valid_arrangements(num_arrangements):
    valid_arrangements = []
    while len(valid_arrangements) < num_arrangements:
        arrangement = generate_random_arrangement()
        if is_valid(arrangement):
            valid_arrangements.append(arrangement)
    return valid_arrangements


if __name__ == '__main__':
    valid_arrangements = generate_valid_arrangements(4)

    for i, arrangement in enumerate(valid_arrangements):
        print(f"Valid arrangement {i+1}: {arrangement}")


