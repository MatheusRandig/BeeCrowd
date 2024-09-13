# https://judge.beecrowd.com/en/problems/view/1037

# returns the interval of the float number
def interval(n):
    if 0 <= n <= 25:
        result = "Intervalo [0,25]"
    elif 25 < n <= 50:
        result = "Intervalo (25,50]"
    elif 50 < n <= 75:
        result = "Intervalo (50,75]"
    elif 75 < n <= 100:
        result = "Intervalo (75,100]"
    else:
        result = "Fora de intervalo"
    return result


# user input
if __name__ == "__main__":
    x = float(input())
    print(interval(x))
