from Python.Problems import beecrowd_1049


# check exercise output
def test_beginner1049_output_print_one() -> None:
    result = beecrowd_1049.output_print(["vertebrado", "mamifero", "onivoro"])
    assert result == "homem"


def test_beginner1049_output_print_two() -> None:
    result = beecrowd_1049.output_print(["vertebrado", "ave", "carnivoro"])
    assert result == "aguia"


def test_beginner1049_output_print_three() -> None:
    result = beecrowd_1049.output_print(["invertebrado", "anelideo", "onivoro"])
    assert result == "minhoca"
