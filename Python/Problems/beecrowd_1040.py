# https://judge.beecrowd.com/en/problems/view/1040


media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10

print(f"Media: {media:.1f}")

if media >= 7:
    print("Aluno aprovado.")

elif media < 5.0:
    print("Aluno reprovado.")

else:
    print("Aluno em exame.")
    exam = float(input())
    print(f"Nota do exame: {exam:.1f}")

    if (media + exam) / 2 >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    print(f"Media final: {((media + exam) / 2):.1f}")


if __name__ == "__name__":
    v = [float(x) for x in input().split()]

    print()
