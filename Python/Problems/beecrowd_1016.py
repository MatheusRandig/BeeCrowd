# https://judge.beecrowd.com/en/problems/view/1016


# Returns the minutes that takes for two cars in different speeds, v2 (bigger) v1 (smaller), to reach set distance (d)
def distance_calc(v1, v2, d):
    return d / ((v2 - v1) / 60)


# Return the exercise output
def output_print(distance):
    return str(int(distance_calc(60, 90, distance))) + " minutos"


# user input
if __name__ == "__main__":
    x = int(input())

    print(output_print(x))
