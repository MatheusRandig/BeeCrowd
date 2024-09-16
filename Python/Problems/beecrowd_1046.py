# https://judge.beecrowd.com/en/problems/view/1046

# returns exercise output
def output_print(a: int, b: int) -> str:
    result = "error"
    if a > b:
        result = "O JOGO DUROU " + str(24 - a + b) + " HORA(S)"
    elif b > a:
        result = "O JOGO DUROU " + str(b - a) + " HORA(S)"
    else:
        result = "O JOGO DUROU 24 HORA(S)"

    return result


# user input
if __name__ == "__main__":
    x = [int(x) for x in input().split()]

    print(output_print(x[0], x[1]))
