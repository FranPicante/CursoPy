from pathlib import Path

# Ruta de la carpeta
carpeta = Path(r"C:\Users\fpetrelli\Documents\py\lista.py")

# Buscar txt
archivos = list(carpeta.glob("*.txt"))

todos = []
unicos = set()

for archivo in archivos:
    with open(archivo, "r", encoding="utf-8") as f:
        for linea in f:
            nombre = linea.strip()

            if nombre:
                todos.append(nombre)
                unicos.add(nombre.lower())

# Guardar todos
with open("todos.txt", "w", encoding="utf-8") as f:
    for nombre in todos:
        f.write(nombre + "\n")

# Guardar únicos
with open("unicos.txt", "w", encoding="utf-8") as f:
    for nombre in sorted(unicos):
        f.write(nombre + "\n")

print("Listo.")
print(f"TXT encontrados: {len(archivos)}")
print(f"Nombres totales: {len(todos)}")
print(f"Nombres únicos: {len(unicos)}")