persona = {"nombre": "Gaby", "edad": 25, "ciudad": "Lincoln"}

print(persona["nombre"])          # leer (si existe la clave)
print(persona.get("telefono"))    # leer seguro (si no existe da None)

persona["edad"] = 26              # actualizar
persona["trabajo"] = "dev"        # agregar nueva clave
print(persona)

for clave, valor in persona.items():
    print(clave, "=>", valor)
