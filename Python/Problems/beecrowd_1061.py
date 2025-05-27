# https://judge.beecrowd.com/en/problems/view/1061

# Calculate the seconds from a given time ( composed of days, hours, minutes, and seconds )
def seconds_in_time(days: int, hours: int, minutes: int, seconds: int) -> int:
    return (days * 86400) + (hours * 3600) + (minutes * 60) + seconds


# Given seconds return days, hours, minutes, and seconds
def time_in_seconds(total: int) -> tuple[int, int, int, int]:
    days = total // 86400
    hours = (total % 86400) // 3600
    minutes = ((total % 86400) % 3600) // 60
    seconds = ((total % 86400) % 3600) % 60

    return (days, hours, minutes, seconds)


# Returns the formatted output string
def exercise_output(days: int, hours: int, minutes: int, seconds: int) -> str:
    return f"{days} dia(s)\n{hours} hora(s)\n{minutes} minuto(s)\n{seconds} segundo(s)"


# Exercise call and print
if __name__ == "__main__":
    # Read the input Line values
    # and split them into days, hours, minutes, and seconds
    day1 = input().split(" ")
    time_day1 = input().split(" ")
    day2 = input().split(" ")
    time_day2 = input().split(" ")

    # Convert the input values to integers and calculate the difference in seconds
    results = time_in_seconds(
        seconds_in_time(int(day2[1]), int(time_day2[0]), int(time_day2[2]), int(time_day2[4]))
        - seconds_in_time(int(day1[1]), int(time_day1[0]), int(time_day1[2]), int(time_day1[4]))
    )

    # Print the formatted output
    print(exercise_output(results[0], results[1], results[2], results[3]))
