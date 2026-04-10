import json

def open_pokemons(pokemons_file):
    with open(pokemons_file, "r", encoding="utf-8") as file:
        pokemons = json.load(file)
    return pokemons


def adding_new_pokemons():
    name=input("Name: ")
    level=input("Level: ")
    tyype=input("Type: ")
    hp=input("HP: ")
    attack=input("Attack: ")
    defense=input("Defense: ")
    sp_attack=input("Sp. Attack: ")
    sp_defense=input("Sp. Defence: ")
    speed=input("Speed: ")

    new_pokemon = {
        "name": {
            "english": name
        },
        "level": level,
        "type": [tyype],
        "base": {
            "HP": hp,
            "Attack": attack,
            "Defense": defense,
            "Sp. Attack": sp_attack,
            "Sp. Defense": sp_defense,
            "Speed": speed
        }
    }
    return new_pokemon


def save_pokemon(pokemons_file, pokemons):
    with open(pokemons_file, "w", encoding="utf-8") as file:
        json.dump(pokemons, file, indent=2)


def main():
    pokemons=open_pokemons("pokemons.json")
    new_pokemon=adding_new_pokemons()
    pokemons.append(new_pokemon)
    save_pokemon("pokemons.json", pokemons)

    print("Pokemon added correctly")


main()