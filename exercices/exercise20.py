

user_info = {"nombre": "Juan Pérez", "edad": 21, "carrera": "Ingeniería en Sistemas", "materias": ["Matemáticas", "Programación", "Física"], "promedio": 8.5}

print("Información del estudiante:")
print(f"Nombre: {user_info['nombre']}")
print(f"Edad: {user_info['edad']} años")
print(f"Carrera: {user_info['carrera']}")
print("Materias:")
for materia in user_info['materias']:
    print(f"- {materia}")

print(f"Promedio: {user_info['promedio']}")

def add_high(high):
   user_info["high"] = high
   print(f"Se ha agregado la altura: {user_info['high']} metros")

add_high(1.75)