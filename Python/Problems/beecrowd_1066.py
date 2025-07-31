# https://judge.beecrowd.com/en/problems/view/1066

# Given 5 numbers return the the count of how many of then are even, odd, negative and positive returning a int list following the order.
def separete_in_bucktes(values: list[int]) -> list[int]:
    par = 0
    impar = 0
    positivo = 0
    negativo = 0
    for i in values:
        if i % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
        if i < 0:
            negativo = negativo + 1
        if i > 0:
            positivo = positivo + 1

    return [par, impar, positivo, negativo]


# Format to excersise
def output_1066(list_input: list[int]) -> str:
    result = separete_in_bucktes(list_input)
    return (
        str(result[0])
        + " valor(es) par(es)"
        + "\n"
        + str(result[1])
        + " valor(es) impar(es)"
        + "\n"
        + str(result[2])
        + " valor(es) positivo(s)"
        + "\n"
        + str(result[3])
        + " valor(es) negativo(s)"
    )


# Exercise call and print
if __name__ == "__main__":
    list_input = [
        int(input()),
        int(input()),
        int(input()),
        int(input()),
        int(input()),
    ]

    print(output_1066(list_input))
