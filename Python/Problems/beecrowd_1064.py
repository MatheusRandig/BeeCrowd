# https://judge.beecrowd.com/en/problems/view/1064

# Given a list returns a tuple with (total, count of positives)
# The function accpets previous values to total and positives numbers, to continue a given average.
def average_of_positives(
    values: list[float], positives_count: int, total: float
) -> tuple[float, int]:
    for i in values:
        if i > 0:
            positives_count = positives_count + 1
            total = total + i
    return total, positives_count


# Format to excersise
def output_1064(list_input: float) -> str:
    result = average_of_positives(list_input, 0, 0)
    if result[1] == 0:
        return "Sem Valores Positivos"
    else:
        return str(result[1]) + " valores positivos\n" + f"{(result[0] / result[1]):.1f}"


# Exercise call and print
if __name__ == "__main__":
    list_input = [
        float(input()),
        float(input()),
        float(input()),
        float(input()),
        float(input()),
        float(input()),
    ]

    print(output_1064(list_input))
