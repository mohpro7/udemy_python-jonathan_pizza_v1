
def add_pizza_user(pizzas):
    user_pizza = input("Ajoutez votre pizza : ")
    print()
    if user_pizza.lower() in [p.lower() for p in pizzas]:
        print("ERREUR: cette pizza existe déjà")
        print()
    else:
        pizzas.append(user_pizza)

def afficher(pizzas, n_first_elements=-1):
    p = pizzas
    if not n_first_elements == -1:
        p = pizzas[:n_first_elements]
    print(f"---- LISTE DES PIZZAS ({len(p)}) ----")
    if len(p) == 0:
        print("aucune pizza")
        return
    else:
        for pizza in p:
            print(pizza)
    print()
    print(f"Première pizza : {pizzas[0]} / Dernière pizza : {pizzas[-1]}")

print()
pizzas = ["4 frmages", "végétarienne", "hawai", "calzone"]
add_pizza_user(pizzas)
afficher(pizzas, 3)