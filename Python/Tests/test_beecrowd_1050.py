from Python.Problems import beecrowd_1050


# check exercise output
def test_beginner1050_find_ddd_one() -> None:
    result = beecrowd_1050.find_ddd("11")
    assert result == "Sao Paulo"


def test_beginner1050_find_ddd_two() -> None:
    result = beecrowd_1050.find_ddd("32")
    assert result == "Juiz de Fora"


def test_beginner1050_find_ddd_three() -> None:
    result = beecrowd_1050.find_ddd("74567456fsdfasdfgdfasd4556he56hg7")
    assert result == "DDD nao cadastrado"
