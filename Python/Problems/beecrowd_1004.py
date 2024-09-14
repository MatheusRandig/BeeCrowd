# https://judge.beecrowd.com/en/problems/view/1004


# returns product value of 2 numbers
def prod(x: int, y: int) -> int:
    return x * y


# print result
def output_print(x: int, y: int) -> str:
    return f"PROD = {prod(x, y)}"


if __name__ == "__main__":
    # input values from user
    x = int(input())
    y = int(input())

    # print result
    print(output_print(x, y))
