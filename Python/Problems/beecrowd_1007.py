#https://judge.beecrowd.com/en/problems/view/1007


# Returns a product of 2 values
def prod(value1,value2):
    return value1*value2


#Returns the Difference
def dif(a,b,c,d):
    return prod(a, b) - prod(c, d)


# print result
def output_print(a,b,c,d):
    return(f"DIFERENCA = {int(dif(a,b,c,d))}")


if __name__ == "__main__":
    # input values from user
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())

    #print result
    print(output_print(a,b,c,d))