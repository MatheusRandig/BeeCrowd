#https://judge.beecrowd.com/en/problems/view/1019

# Returns hours in SEConds
def seconds_to_hours(sec):
    return sec // 3600

# Returns minutes in SEConds
def seconds_to_minutes(sec):
    return sec // 60

# Returns the exercise output
def output_print(sec):

    hour = seconds_to_hours(sec)
    result = str(hour)+":"
    sec = sec-(hour*3600)

    minutes = seconds_to_minutes(sec)
    result += str(minutes)+":"
    sec = sec-(minutes*60)

    result += str(sec)
    return result

# user input
if __name__ == "__main__":

    x = int(input())
    print(output_print(x))