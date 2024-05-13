def calculate_squares(start, end):
    for i in range(start, end):
        squared = i * i
        print(f"{i} squared = {squared}")


# Don't edit below this line


def test(start, end):
    print(f"Using inputs start: {start} and end: {end}")
    print(f"Calculating squares from {start} to {end - 1}")
    calculate_squares(start, end)
    print("=====================================")


def main():
    test(100, 105)
    test(1, 3)
    test(11, 14)


main()

