# https://judge.beecrowd.com/en/problems/view/1036


# Returns the R1 and R2 of bhaskara, if not possible return "Impossivel calcular"
def bhaskara(A: float, B: float, C: float, decimal: int) -> str:
    delta = (B**2) - 4 * A * C

    if delta > 0 and A != 0:
        r1 = ((-B) + (delta**0.5)) / (2 * A)
        r2 = ((-B) - (delta**0.5)) / (2 * A)
        result = "R1 = " + ("{:." + str(decimal) + "f}").format(r1) + "\n"
        result += "R2 = " + ("{:." + str(decimal) + "f}").format(r2)
    else:
        result = "Impossivel calcular"
    return result


# user input
if __name__ == "__main__":
    A, B, C = [float(x) for x in input().split()]

    print(bhaskara(A, B, C, 5))
