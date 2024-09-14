# https://judge.beecrowd.com/en/problems/view/1041

# Returns the exercise output
def output_print(x: float, y: float) -> str:
    result = ""
    if x == 0 and y == 0:
        result = "Origem"

    elif x == 0 and y != 0:
        result = "Eixo Y"

    elif x != 0 and y == 0:
        result = "Eixo X"

    elif x > 0 and y > 0:
        result = "Q1"

    elif x < 0 and y > 0:
        result = "Q2"

    elif x > 0 and y < 0:
        result = "Q4"

    elif x < 0 and y < 0:
        result = "Q3"

    return result


# User Input
if __name__ == "__main__":
    x = [float(x) for x in input().split()]

    print(output_print(x[0], x[1]))
