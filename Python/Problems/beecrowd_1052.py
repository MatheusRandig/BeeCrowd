# https://judge.beecrowd.com/en/problems/view/1052

# Returns the month of n argument
def n_to_month(n: int) -> str:
    month = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }

    return month[n]


if __name__ == "__main__":
    x = int(input())
    print(n_to_month(x))
