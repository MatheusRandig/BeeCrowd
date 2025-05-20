# https://judge.beecrowd.com/en/problems/view/1060

# count positive numbers based on 6 inputs
def positive_numbers(numbers: list[float]) -> int:
    count = 0
    for n in numbers:
        if float(n) > 0:
            count += 1
    return count


# Exercise call and print
if __name__ == "__main__":
    print(
        f"{positive_numbers([float(input()), float(input()), float(input()), float(input()), float(input()), float(input())])} valores positivos"
    )
