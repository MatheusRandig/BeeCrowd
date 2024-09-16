# https://judge.beecrowd.com/en/problems/view/1045

# returns true if not triangle
def not_triangle(a: float, b: float, c: float) -> bool:
    if a >= (b + c):
        return True
    else:
        return False


# returns true if is rectangle triangle
def rectangle_triangle(a: float, b: float, c: float) -> bool:
    if (a * a) == ((b * b) + (c * c)):
        return True
    else:
        return False


# returns true if is obtuse triangle
def obtuse_triangle(a: float, b: float, c: float) -> bool:
    if (a * a) > ((b * b) + (c * c)):
        return True
    else:
        return False


# returns true if is acute triangle
def acute_triangle(a: float, b: float, c: float) -> bool:
    if (a * a) < ((b * b) + (c * c)):
        return True
    else:
        return False


# returns true if is equilateral triangle
def equilateral_triangle(a: float, b: float, c: float) -> bool:
    if a == b and b == c and c == a:
        return True
    else:
        return False


# returns true if is isosceles triangle
def isosceles_triangle(a: float, b: float, c: float) -> bool:
    if a == b or b == c or c == a:
        return True
    else:
        return False


# returns the exercise output
def output_print(a: float, b: float, c: float) -> str:
    result = ""
    if not_triangle(a, b, c):
        result += "NAO FORMA TRIANGULO"
    else:
        if rectangle_triangle(a, b, c):
            result += "TRIANGULO RETANGULO"
        elif obtuse_triangle(a, b, c):
            result += "TRIANGULO OBTUSANGULO"
        elif acute_triangle(a, b, c):
            result += "TRIANGULO ACUTANGULO"

        if equilateral_triangle(a, b, c):
            result += "\nTRIANGULO EQUILATERO"
        elif isosceles_triangle(a, b, c):
            result += "\nTRIANGULO ISOSCELES"

    return result


# user input
if __name__ == "__main__":
    v = [float(x) for x in input().split()]
    v.sort()

    print(output_print(v[2], v[1], v[0]))
