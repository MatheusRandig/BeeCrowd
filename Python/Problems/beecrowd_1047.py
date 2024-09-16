# https://judge.beecrowd.com/en/problems/view/1047

# returns exercise input
def output_print(minutes1: int, minutes2: int) -> str:
    result = ""
    if minutes1 == minutes2:
        result += "O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)"
    elif minutes1 > minutes2:
        result += (
            "O JOGO DUROU "
            + str((1440 - minutes1 + minutes2) // 60)
            + " HORA(S) E "
            + str((1440 - minutes1 + minutes2) % 60)
            + " MINUTO(S)"
        )
    else:
        result += (
            "O JOGO DUROU "
            + str((minutes2 - minutes1) // 60)
            + " HORA(S) E "
            + str((minutes2 - minutes1) % 60)
            + " MINUTO(S)"
        )
    return result


# user input
if __name__ == "__main__":
    a, b, c, d = [int(x) for x in input().split()]

    x = (a * 60) + b
    y = (c * 60) + d

    print(x, y)
    print(output_print(x, y))
