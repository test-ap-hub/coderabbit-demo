def calculate_average(numbers):
    total = 0

    for num in numbers:
        total += num

    return total / len(numbers)


def main():
    scores = [90, 85, 92]
    avg = calculate_average(scores)
    print(f"Average: {avg}")


if __name__ == "__main__":
    main()
