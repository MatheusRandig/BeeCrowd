# https://judge.beecrowd.com/en/problems/view/1012

# Using sides, Returns the area of a rectangle triangle
# digits is the accuracy of the float
def area_rectangle_triangle(side_a, side_b, digits):
    return ("{:." + str(digits) + "f}").format(side_a * side_b * 0.5)


# Using radius, Returns the area of a circle
# digits is the accuracy of the float
def area_circle(r, digits):
    return ("{:." + str(digits) + "f}").format(r * r * 3.14159)


# Using bases and height, Returns the area of a trapezium
# digits is the accuracy of the float
def area_trapezium(base_a, base_b, height, digits):
    return ("{:." + str(digits) + "f}").format((base_a + base_b) / 2 * height)


# Using side, Returns the area of a square
# digits is the accuracy of the float
def area_square(side, digits):
    return ("{:." + str(digits) + "f}").format(side * side)


# Using sides, Returns the area of a rectangle
# digits is the accuracy of the float
def area_rectangle(side_a, side_b, digits):
    return ("{:." + str(digits) + "f}").format(side_a * side_b)


# Returns the exercise output
def output_print(a, b, c):
    return (
        f"TRIANGULO: {area_rectangle_triangle(a, c,3)}\n"
        f"CIRCULO: {area_circle(c,3)}\n"
        f"TRAPEZIO: {area_trapezium(a,b,c,3)}\n"
        f"QUADRADO: {area_square(b,3)}\n"
        f"RETANGULO: {area_rectangle(a,b,3)}"
    )


# user input
if __name__ == "__main__":
    v = [float(x) for x in input().split()]

    print(output_print(v[0], v[1], v[2]))
