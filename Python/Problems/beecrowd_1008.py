#https://judge.beecrowd.com/en/problems/view/1008


#Number
def employee_number(x):
    return("NUMBER = "+str(x))

def salary(y,z):
    result = '{:.2f}'.format(y*z)
    return("SALARY = U$ "+str(result))


if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = float(input())

    print(employee_number(x))
    print(salary(y,z))