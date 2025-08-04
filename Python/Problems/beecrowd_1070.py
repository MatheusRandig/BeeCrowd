# https://judge.beecrowd.com/en/problems/view/1070

# Given int n return a int list of next 6 odd numbers
def next_six_odd(n: int) -> list[int]:
    next_six_odd = []

    if n % 2 == 0:
        n += 1
    for i in range(6):
        next_six_odd.append(n + i + i)

    return next_six_odd


# Format to excersive expected output
def output_1070(n: int) -> str:
    odd_list = next_six_odd(n)

    result = ""
    for i in odd_list:
        result += str(i) + "\n"

    # remove last \n"
    result = result[:-1]
    return result


# Exercise call and print
if __name__ == "__main__":
    n = int(input())

    print(output_1070(n))
