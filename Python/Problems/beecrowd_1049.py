# https://judge.beecrowd.com/en/problems/view/1049

# Returns exercise output
def output_print(v: list[str]) -> str:
    # creates exercise tree
    tree = {
        "vertebrado": {
            "ave": {"carnivoro": "aguia", "onivoro": "pomba"},
            "mamifero": {"onivoro": "homem", "herbivoro": "vaca"},
        },
        "invertebrado": {
            "inseto": {"hematofago": "pulga", "herbivoro": "lagarta"},
            "anelideo": {"hematofago": "sanguessuga", "onivoro": "minhoca"},
        },
    }

    return tree[v[0]][v[1]][v[2]]


# user input
if __name__ == "__main__":
    a = input()
    b = input()
    c = input()

    print(output_print([a, b, c]))
