# https://judge.beecrowd.com/en/problems/view/1048

# return the exercise output
def output_print(salary: float) -> str:
    result = ""
    if salary <= 400:
        new = "{:.2f}".format(salary * 1.15)
        adjust = "{:.2f}".format(salary * 0.15)
        result = "Novo salario: " + new + "\nReajuste ganho: " + adjust + "\nEm percentual: 15 %"
    elif salary <= 800:
        new = "{:.2f}".format(salary * 1.12)
        adjust = "{:.2f}".format(salary * 0.12)
        result = "Novo salario: " + new + "\nReajuste ganho: " + adjust + "\nEm percentual: 12 %"
    elif salary <= 1200:
        new = "{:.2f}".format(salary * 1.10)
        adjust = "{:.2f}".format(salary * 0.10)
        result = "Novo salario: " + new + "\nReajuste ganho: " + adjust + "\nEm percentual: 10 %"
    elif salary <= 2000:
        new = "{:.2f}".format(salary * 1.07)
        adjust = "{:.2f}".format(salary * 0.07)
        result = "Novo salario: " + new + "\nReajuste ganho: " + adjust + "\nEm percentual: 7 %"
    else:
        new = "{:.2f}".format(salary * 1.04)
        adjust = "{:.2f}".format(salary * 0.04)
        result = "Novo salario: " + new + "\nReajuste ganho: " + adjust + "\nEm percentual: 4 %"
    return result


# user input
if __name__ == "__main__":
    x = float(input())

    print(output_print(x))
