# https://judge.beecrowd.com/en/problems/view/1071


# Given two ints, return the sum of the all odd numbers in between
def sum_odd_in_between(x: int, y: int) -> int:
    if x > y:
        v = list(range(y + 1, x))
    else:
        v = list(range(x + 1, y))

    total = 0
    for i in v:
        if i % 2 != 0:
            total = total + i
    return total


# Exercise call and print
if __name__ == "__main__":
    x = int(input())
    y = int(input())

    print(sum_odd_in_between(x, y))
