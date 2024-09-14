# https://judge.beecrowd.com/en/problems/view/1014

# Returns the km/fuel with precisions of digits
def liter_km(km: int, fuel: float, digits: int) -> str:
    return ("{:." + str(digits) + "f}").format(km / fuel)


# Returns the exercise output
def output_print(km: int, fuel: float) -> str:
    return str(liter_km(km, fuel, 3)) + " km/l"


# user input
if __name__ == "__main__":
    x = int(input())
    y = float(input())

    print(output_print(x, y))
