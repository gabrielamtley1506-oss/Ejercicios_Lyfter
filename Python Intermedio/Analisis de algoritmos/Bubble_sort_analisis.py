# Analisis del algoritmo


def bubble_sort(list_to_sort): # diriamos que esta funcion es o (n^2)
    for outer_index in range(0, len(list_to_sort)-1): # o(n)
        has_made_changes = False # o(1)
        for index in range(0, len(list_to_sort)-1 - outer_index): # o(n^2)
            current_element = list_to_sort[index] # o(1)
            next_element = list_to_sort[index +1] # o(1)

            print(f"Iteracion {outer_index}, {index}, Elemento actual {current_element}, Siguiente elemento {next_element}") # o(1)

            if current_element > next_element: # o(1)
                print("El elemento actual es mayor al siguiente y cambiamos posiciones") # o(1)
                list_to_sort[index] = next_element # o(1)
                list_to_sort[index +1] = current_element # o(1)
                has_made_changes=True # o(1)

        if not has_made_changes: # o(1)
                return

my_test_list = [18, -11, 68, 6, 32, 53, -2] # o(1)
bubble_sort(my_test_list) # o(n^2)
print(my_test_list) # o(1)


# En conclusion podemos ver que este algoritmo es de o(n^2) por tener dos ciclos anidados
