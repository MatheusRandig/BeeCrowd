# https://judge.beecrowd.com/en/problems/view/1035

# Uses the exercise logic to determine if the numbers are acceptable or not
def selection_test(A, B, C, D):
    if B > C and D > A and C + D > A + B and C >= 0 and D >= 0 and A % 2 == 0:
        return "Valores aceitos"
    else:
        return "Valores nao aceitos"


# user input
if __name__ == "__main__":
    A, B, C, D = [int(x) for x in input().split()]

    print(selection_test(A, B, C, D))
