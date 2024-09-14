# https://judge.beecrowd.com/en/problems/view/1040

# Returns a float of the average notes of a student
def average_student(n1: float, n2:float, n3: float, n4: float, decimal: int) -> float:
    return round(((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10, decimal)

# Calculate if a student is approved or failed after exam
def recu_student(average: float,  exam: float, decimal: int) -> str:
    if (average + exam) / 2 >= 5:
        result = "\nAluno aprovado."
    else:
        result = "\nAluno reprovado."
    result +="\nMedia final: "+str(round((average + exam) / 2, decimal))
    return result


#Print exercise output as intended
def output_print(n1: float, n2: float, n3: float, n4: float) -> str:
    average = average_student(n1, n2, n3, n4, 1)
    result="Media: "+str(average)

    if average >= 7:
        result += "\nAluno aprovado."

    elif average < 5.0:
        result += "\nAluno reprovado."

    else:
        result += "\nAluno em exame."
        exam = float(input())
        result += "\nNota do exame: "+f"{exam:.1f}"
        result += recu_student(average, exam, 1)

    return result

if __name__ == "__main__":

    v = [float(x) for x in input().split()]

    print(output_print(v[0], v[1], v[2], v[3]))

