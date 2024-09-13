from Python.Problems import beecrowd_1036


# check exercise logic and output
def test_beginner1036_bhaskara_one():
    result = beecrowd_1036.bhaskara(10.0, 20.1, 5.1, 5)
    assert result == "R1 = -0.29788\nR2 = -1.71212"


def test_beginner1036_bhaskara_two():
    result = beecrowd_1036.bhaskara(0.0, 20.0, 5.0, 5)
    assert result == "Impossivel calcular"


def test_beginner1036_bhaskara_three():
    result = beecrowd_1036.bhaskara(10.3, 203.0, 5.0, 5)
    assert result == "R1 = -0.02466\nR2 = -19.68408"


def test_beginner1036_bhaskara_four():
    result = beecrowd_1036.bhaskara(10.0, 3.0, 5.0, 5)
    assert result == "Impossivel calcular"
