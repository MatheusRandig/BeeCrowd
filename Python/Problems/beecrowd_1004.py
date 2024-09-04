#https://judge.beecrowd.com/en/problems/view/1004


# returns product value of 2 numbers
def prod(x,y):
    return x*y

# print result
def output_print(x,y):
    return(f"PROD = {prod(x,y)}")


if __name__ == "__main__":
    # input values from user
    x = int(input())
    y = int(input())

    #print result
    print(output_print(x,y))