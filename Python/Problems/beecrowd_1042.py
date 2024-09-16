# https://judge.beecrowd.com/en/problems/view/1042

# returns the sort string
def sorter(s: list[int]) -> str:
    s.sort()
    return str(s[0]) + "\n" + str(s[1]) + "\n" + str(s[2])


# returns the expected output
def output_print(v: list[int]) -> str:
    result = "\n\n" + str(v[0]) + "\n" + str(v[1]) + "\n" + str(v[2])
    result = sorter(v) + result

    return result


# user input
if __name__ == "__main__":
    v = [int(x) for x in input().split()]

    print(output_print(v))
