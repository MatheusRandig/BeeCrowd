from Python.Problems import beecrowd_1016


# check distance calc
def test_beginner1016_distance_calc_one():
    result = beecrowd_1016.distance_calc(60, 90, 30)
    assert result == 60.0


def test_beginner1016_distance_calc_two():
    result = beecrowd_1016.distance_calc(60, 90, 110)
    assert result == 220.0


def test_beginner1016_distance_calc_three():
    result = beecrowd_1016.distance_calc(60, 90, 7)
    assert result == 14.0


# check exercise output
def test_beginner1016_print_one():
    result = beecrowd_1016.output_print(30)
    assert result == "60 minutos"


def test_beginner1016_print_two():
    result = beecrowd_1016.output_print(110)
    assert result == "220 minutos"


def test_beginner1016_print_three():
    result = beecrowd_1016.output_print(7)
    assert result == "14 minutos"
