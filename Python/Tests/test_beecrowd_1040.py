from Python.Problems import beecrowd_1040


# check student average function
def test_beginner1040_average_student_one() -> None:
    result = beecrowd_1040.average_student(2.0, 4.0, 7.5, 8.0, 1)
    assert result == 5.4


def test_beginner1040_average_student_two() -> None:
    result = beecrowd_1040.average_student(2.0, 6.5, 4.0, 9.0, 1)
    assert result == 4.8


def test_beginner1040_average_student_three() -> None:
    result = beecrowd_1040.average_student(9.0, 4.0, 8.5, 9.0, 1)
    assert result == 7.3


# check recu student function with approved and failed
def test_beginner1040_recu_student_one() -> None:
    result = beecrowd_1040.recu_student(5.4, 6.4, 1)
    assert result == "\nAluno aprovado.\nMedia final: 5.9"


def test_beginner1040_recu_student_two() -> None:
    result = beecrowd_1040.recu_student(5.4, 0, 1)
    assert result == "\nAluno reprovado.\nMedia final: 2.7"


# check desired output
def test_beginner1040_output_print_one(monkeypatch) -> None:
    monkeypatch.setattr("builtins.input", lambda: 6.4)
    result = beecrowd_1040.output_print(2.0, 4.0, 7.5, 8.0)
    assert (
        result
        == "Media: 5.4\nAluno em exame.\nNota do exame: 6.4\nAluno aprovado.\nMedia final: 5.9"
    )


def test_beginner1040_output_print_two() -> None:
    result = beecrowd_1040.output_print(2.0, 6.5, 4.0, 9.0)
    assert result == "Media: 4.8\nAluno reprovado."


def test_beginner1040_output_print_three() -> None:
    result = beecrowd_1040.output_print(9.0, 4.0, 8.5, 9.0)
    assert result == "Media: 7.3\nAluno aprovado."
