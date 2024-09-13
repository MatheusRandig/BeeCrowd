# https://judge.beecrowd.com/en/problems/view/1003

# returns added value of 2 numbers
def addition(x, y):
    return x + y


# print result
def output_print(x, y):
    return f"SOMA = {addition(x,y)}"


if __name__ == "__main__":
    # input values from user
    x = int(input())
    y = int(input())

    # print result
    print(output_print(x, y))
