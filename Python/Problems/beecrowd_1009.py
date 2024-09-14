# https://judge.beecrowd.com/en/problems/view/1009


# Returns a float of the total salary
# The total is fixed salary + 15% of commissions of the monthly sell
def total_salary(fixed_salary: float, month_sells: float) -> str:
    return "{:.2f}".format(fixed_salary + (month_sells * 0.15))


# output salary
def output_print(salary: float, sells: float) -> str:
    return "TOTAL = R$ " + total_salary(salary, sells)


# user input
if __name__ == "__main__":
    name = input()
    salary = float(input())
    sells = float(input())

    print(output_print(salary, sells))
