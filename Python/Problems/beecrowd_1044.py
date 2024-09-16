# https://judge.beecrowd.com/en/problems/view/1044

# Returns true if the numbers are multiples, false otherwise
def multiples(a: int, b: int) -> bool:
    if (a % b == 0) or (b % a == 0):
        return True
    else:
        return False


# returns exercise output
def output_print(v: list[int]) -> str:
    if multiples(v[0], v[1]):
        return "Sao Multiplos"
    else:
        return "Nao sao Multiplos"


# user input
if __name__ == "__main__":
    v = [int(x) for x in input().split()]

    print(output_print(v))
