from Python.Problems import beecrowd_1061


# check seconds_in_time of exercise 1061
def test_beginner1061_seconds_in_time_one() -> None:
    result = beecrowd_1061.seconds_in_time(0, 0, 5, 0)
    assert result == 300


def test_beginner1061_seconds_in_time_two() -> None:
    result = beecrowd_1061.seconds_in_time(5, 8, 12, 23)
    assert result == 461543


# check time_in_seconds of exercise 1061
def test_beginner1061_time_in_seconds_one() -> None:
    result = beecrowd_1061.time_in_seconds(300)
    assert result == (0, 0, 5, 0)


def test_beginner1061_time_in_seconds_two() -> None:
    result = beecrowd_1061.time_in_seconds(461543)
    assert result == (5, 8, 12, 23)


# check exercise_output of exercise 1061
def test_beginner1061_exercise_output_one() -> None:
    result = beecrowd_1061.exercise_output(5, 8, 12, 23)
    assert result == "5 dia(s)\n8 hora(s)\n12 minuto(s)\n23 segundo(s)"


def test_beginner1061_exercise_output_two() -> None:
    result = beecrowd_1061.exercise_output(0, 0, 5, 0)
    assert result == "0 dia(s)\n0 hora(s)\n5 minuto(s)\n0 segundo(s)"
