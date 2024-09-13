# https://judge.beecrowd.com/en/problems/view/1015


def distance_points(x, y, digits):
    x1, y1 = [float(i) for i in x.split()]
    x2, y2 = [float(i) for i in y.split()]

    result = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    return ("{:." + str(digits) + "f}").format(result)


# user input
if __name__ == "__main__":
    x = input()
    y = input()

    print(distance_points(x, y, 4))
