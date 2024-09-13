# https://judge.beecrowd.com/en/problems/view/1020

# Returns years of days
def days_to_years(days):
    return days // 365


# Returns month of days
def days_to_month(days):
    return days // 30


# Returns the exercise output
def output_print(days):
    years = days_to_years(days)
    result = str(years) + " ano(s)\n"
    days -= years * 365

    months = days_to_month(days)
    result += str(months) + " mes(es)\n"
    days -= months * 30

    result += str(days) + " dia(s)"
    return result


# user input
if __name__ == "__main__":
    x = int(input())
    print(output_print(x))
