# https://judge.beecrowd.com/en/problems/view/1001

# addition
def beginner1001_sum(x: int, y: int) -> int:
    return x + y


# print result
def beginner1001_print(x: int, y: int) -> str:
    return f"X = {beginner1001_sum(x, y)}"


if __name__ == "__main__":
    # input values from user
    x = int(input())
    y = int(input())

    # print result
    print(beginner1001_print(x, y))
