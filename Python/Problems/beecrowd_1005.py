# https://judge.beecrowd.com/en/problems/view/1005


# returns average value of 2 numbers
# Value1 has 3.5 weight
# Value2 has 7.5 weight
def average_35_75(value1: float, value2: float, digits: int) -> str:
    result = ("{:." + str(digits) + "f}").format(((value1 * 3.5) + (value2 * 7.5)) / 11)
    return result


# print result
def output_print(x: float, y: float) -> str:
    return f"MEDIA = {average_35_75(x,y,5)}"


if __name__ == "__main__":
    # input values from user
    x = float(input())
    y = float(input())

    # print result
    print(output_print(x, y))
