# https://judge.beecrowd.com/en/problems/view/1043

# Returns the perimeter of a triangle
def perimeter(a: float, b: float, c: float) -> float:
    return a + b + c


# Returns the area of a triangle
def area(a: float, b: float, c: float) -> float:
    return ((a + b) * c) / 2


# Returns output of the exercise
def output_print(v: list[float]) -> str:
    if 4 * v[0] * v[0] * v[1] * v[1] > ((v[0] * v[0]) + (v[1] * v[1]) - (v[2] * v[2])) ** 2:
        x = perimeter(v[0], v[1], v[2])

        result = "Perimetro = " + str("{:.1f}".format(x))
    else:
        x = area(v[0], v[1], v[2])
        result = "Area = " + str("{:.1f}".format(x))
    return result


if __name__ == "__main__":
    v = [float(x) for x in input().split()]

    print(output_print(v))
