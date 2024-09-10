from Python.Problems import beecrowd_1019

# check seconds to hour function
def test_beginner1019_seconds_to_hours_one():
    result = beecrowd_1019.seconds_to_hours(556)
    assert result == 0

def test_beginner1019_seconds_to_hours_two():
    result = beecrowd_1019.seconds_to_hours(1)
    assert result == 0

def test_beginner1019_seconds_to_hours_three():
    result = beecrowd_1019.seconds_to_hours(140153)
    assert result == 38


# check seconds to minutes function
def test_beginner1019_seconds_to_minutes_one():
    result = beecrowd_1019.seconds_to_minutes(556)
    assert result == 9

def test_beginner1019_seconds_to_minutes_two():
    result = beecrowd_1019.seconds_to_minutes(1)
    assert result == 0

def test_beginner1019_seconds_to_minutes_three():
    result = beecrowd_1019.seconds_to_minutes(3353)
    assert result == 55



# check output of the exercise
def test_beginner1019_output_print_one():
    result = beecrowd_1019.output_print(556)
    assert result == '0:9:16'

def test_beginner1019_output_print_two():
    result = beecrowd_1019.output_print(1)
    assert result == '0:0:1'

def test_beginner1019_output_print_three():
    result = beecrowd_1019.output_print(140153)
    assert result == '38:55:53'

