# https://judge.beecrowd.com/en/problems/view/1002

# Circle area
def circle_area(r, digits):
    result = ('{:.'+str(digits)+'f}').format(r*r*3.14159)
    return result

# print result
def output_print(x):
    return(f"A={circle_area(x,4)}")


if __name__ == "__main__":
    # input radius from use
    x = float(input())

    #print result
    print(output_print(x))