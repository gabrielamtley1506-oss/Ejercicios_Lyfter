import csv

def how_many():
    while True:
        try:
            cant = int(input("¿Cuántos videojuegos quieres ingresar? "))
            if cant > 0:
                return cant
            else:
                print("Ingresa un número mayor que 0.")
        except ValueError:
            print("Error: debes ingresar un número entero.")


def video_games(num):
    print(f"\nVideojuego {num}")
    
    name = input("Nombre: ")
    genre = input("Género: ")
    dev = input("Desarrollador: ")
    classification = input("Clasificación ESRB: ")
    
    return {
        "nombre": name,
        "genero": genre,
        "desarrollador": dev,
        "clasificacion": classification
    }


def save_csv(games_list, file_name="games.csv"):
    with open(file_name, "w", newline="", encoding="utf-8") as archive:
        fields = ["nombre", "genero", "desarrollador", "clasificacion"]
        writer = csv.DictWriter(archive, fieldnames=fields)
        
        writer.writeheader()
        writer.writerows(games_list)


def main():
    games = []
    
    cant = how_many()
    
    for i in range(1, cant + 1):
        games.append(video_games(i))
    
    save_csv(games)
    print("\nLos datos se guardaron correctamente en 'games.csv'.")


main()