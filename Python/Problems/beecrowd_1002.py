# https://judge.beecrowd.com/en/problems/view/1002

# Circle area
def beginner1002_(x):
    return x*x*3.14159

# print result
def beginner1002_print(x,y):
    return(f"X = {beginner1002(x,y)}")


if __name__ == "__main__":
    # input radius from use
    x = float(input())

    #print result
    print(beginner1002_print(x))