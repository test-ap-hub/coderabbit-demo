import time


def calculate_average(numbers):
    total = 0

    for num in numbers:
        total += num

    return total / len(numbers)


def process_user_data(users):
    result = []

    for user in users:
        if "name" in user:
            result.append(user["name"])

    return result


def unused_function():
    time.sleep(5)
    return "unused"


def main():
    scores = []

    avg = calculate_average(scores)

    print(avg)

    users = [
        {"name": "Alice"},
        {"name": "Bob"},
        {},
    ]

    names = process_user_data(users)

    print(names)


if __name__ == "__main__":
    main()
