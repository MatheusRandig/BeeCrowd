# https://judge.beecrowd.com/en/problems/view/1065

# Given 5 numbers return the the count of how many of then are even
def count_between_5(values: list[float]) -> int:
    count = 0
    for i in values:
        if i % 2 == 0:
            count = count + 1
    return count


# Format to excersise
def output_1065(list_input: list[float]) -> str:
    result = count_between_5(list_input)
    return str(result) + " valores pares"


# Exercise call and print
if __name__ == "__main__":
    list_input = [
        float(input()),
        float(input()),
        float(input()),
        float(input()),
        float(input()),
    ]

    print(output_1065(list_input))
