# https://judge.beecrowd.com/en/problems/view/1011

# Returns Volume of the Circle
def volume_circle(radius: float, decimal: int) -> str:
    return ("{:." + str(decimal) + "f}").format((radius**3) * 3.14159 * 4 / 3)


# Returns Exercise output
def output_print(r: float) -> str:
    return "VOLUME = " + str(volume_circle(r, 3))


# user input
if __name__ == "__main__":
    r = float(input())

    print(output_print(r))
