# https://judge.beecrowd.com/en/problems/view/1067

# Given int n return a list of all odd number from 0 to n
def odd_zero_to_range(n: int) -> list[int]:
    odd_numbers = []
    for i in range(n + 1):
        if i % 2 != 0:
            odd_numbers.append(i)
    return odd_numbers


# Format to excersive expected output
def output_1067(n: int) -> str:
    odd_list = odd_zero_to_range(n)

    result = ""
    for i in odd_list:
        result += str(i) + "\n"

    # remove last \n"
    result = result[:-1]
    return result


# Exercise call and print
if __name__ == "__main__":
    n = int(input())

    print(output_1067(n))
