# https://judge.beecrowd.com/en/problems/view/1059

# Returns 0 to 100 number divided by line
def zero_to_hundred() -> str:
    result = ""
    for i in range(49):
        result += str((i + 1) * 2) + "\n"
    return result + "100"


# Exercise call and print
if __name__ == "__main__":
    print(zero_to_hundred())
