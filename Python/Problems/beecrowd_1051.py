# https://judge.beecrowd.com/en/problems/view/1051

# returns taxes of salary
def taxes(n: float) -> str:
    if n < 2000:
        return "Isento"
    else:
        if n < 3000:
            tax = "{:.2f}".format((n - 2000) * 0.08)
        elif n < 4500:
            tax = "{:.2f}".format(80 + ((n - 3000) * 0.18))
        else:
            tax = "{:.2f}".format(80 + 270 + ((n - 4500) * 0.28))
        return "R$ " + tax


# use input
if __name__ == "__main__":
    x = float(input())

    print(taxes(x))
