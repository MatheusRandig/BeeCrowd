# https://judge.beecrowd.com/en/problems/view/1017


# Returns amount of fuel need for a trip
def liter_needed(hours, km, usage, decimal):
    result = km * hours / usage
    return ("{:." + str(decimal) + "f}").format(result)


# user input
if __name__ == "__main__":
    x = int(input())
    y = int(input())

    print(liter_needed(x, y, 12, 3))
