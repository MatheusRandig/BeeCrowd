# https://judge.beecrowd.com/en/problems/view/1007


# Returns a product of 2 values
def prod(value1: int, value2: int) -> int:
    return value1 * value2


# Returns the Difference
def dif(a: int, b: int, c: int, d: int) -> int:
    return prod(a, b) - prod(c, d)


# print result
def output_print(a: int, b: int, c: int, d: int) -> str:
    return f"DIFERENCA = {int(dif(a,b,c,d))}"


if __name__ == "__main__":
    # input values from user
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    # print result
    print(output_print(a, b, c, d))
