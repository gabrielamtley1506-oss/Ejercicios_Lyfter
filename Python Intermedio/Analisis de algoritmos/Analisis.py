#EStaremos analisando varios algoritmos:

def print_numbers_times_2(numbers_list):# o(n) "Porque el ciclo va a ejecutarse siempre n cantidad de veces"
	for number in numbers_list: # o(n)
		print(number * 2) # o(1)
		
###################################################


def check_if_lists_have_an_equal(list_a, list_b): # o(n^2)
	for element_a in list_a: # o(n) " Aunque sea un ciclo que solo se va a correr en determinacion de la lista, no tenemos conocimiento del tamaño de la lista"
		for element_b in list_b: # o(n^2)
			if element_a == element_b:# o(1)
				return True # o(1)
				
	return False # o(1)
####################################################

def print_10_or_less_elements(list_to_print): # o(1)
	list_len = len(list_to_print) # o(1)
	for index in range(min(list_len, 10)): # o(1) "Porque el ciclo es lineal siempre va a ser menor o igual a 10"
		print(list_to_print[index]) # o(1)
		
####################################################


def generate_list_trios(list_a, list_b, list_c):# o(n^3)
	result_list = [] # o(1)
	for element_a in list_a: # o(n)
		for element_b in list_b:# o(n^2)
			for element_c in list_c:# o(n^3) "Son tres ciclos anidados"
				result_list.append(f'{element_a} {element_b} {element_c}') # o(1)
				
	return result_list # o(1)