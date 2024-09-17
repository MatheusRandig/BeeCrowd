# https://judge.beecrowd.com/en/problems/view/1050

# returns the name of the city of argument
def find_ddd(n: str) -> str:
    ddd = {
        "61": "Brasilia",
        "71": "Salvador",
        "11": "Sao Paulo",
        "21": "Rio de Janeiro",
        "32": "Juiz de Fora",
        "19": "Campinas",
        "27": "Vitoria",
        "31": "Belo Horizonte",
    }

    if n in ddd:
        return ddd[n]
    else:
        return "DDD nao cadastrado"


# user input
if __name__ == "__main__":
    x = input()

    print(find_ddd(x))
