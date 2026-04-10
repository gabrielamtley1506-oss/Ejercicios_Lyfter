# Cree un diccionario con una lista dentro

hotel={
    'name': 'Melia',
    'stars_number': 5,
    'rooms': [ 
        room_1 := {
            'number': 101,
            'floor': 1,
            'price_per_night': 150.0,
        },
        room_2 := {
            'number': 202,
            'floor': 2,
            'price_per_night': 200.0,
        },
        room_3 := {
            'number': 303,
            'floor': 3,
            'price_per_night': 250.0,
        },
    ],
}

print(hotel)