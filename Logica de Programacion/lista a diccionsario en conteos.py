palabras = ["hola", "chat", "hola", "python", "chat", "hola"]

conteo = {}
for p in palabras:
    conteo[p] = conteo.get(p, 0) + 1

print(conteo)  # esperado: {'hola': 3, 'chat': 2, 'python': 1}
