# https://judge.beecrowd.com/en/problems/view/1038

# Menu with prices of each code
def snack_menu(code, quantity):
    match code:
        case 1:
            value = 4.00
        case 2:
            value = 4.50
        case 3:
            value = 5.00
        case 4:
            value = 2.00
        case 5:
            value = 1.50
        case _:
            value = 0.00

    return value * quantity


# returns the output of the exercise
def output_print(x, y):
    return "Total: R$ " + str("{:.2f}".format(snack_menu(x, y)))


# User input
if __name__ == "__main__":
    x, y = [float(x) for x in input().split()]

    print(output_print(x, y))
