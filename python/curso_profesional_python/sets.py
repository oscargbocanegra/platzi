# Creando elementos sets
my_set = {3,4,5}
print(f'Creando elementos set1 {my_set}')

#Creando set con elementos unicos e inmutables
my_set2 = {"Hola", 23.3, False, True}
print(f'Creando set con elementos unicos inmutables set2 {my_set2}')

#Creando sets con elementos repetidos
my_set3 = {3,3,2}
print(f'Creando sets con elementos repetidos set3 {my_set3}')

#Creando sets con una lista elemento mutable que genera error.
#my_set4 = {[1,2,3],4}
#print(f'Creando sets con elementos repetidos {my_set4}')

#Convirtiendo una estructura de datos a sets
my_list = [1,1,2,3,4,4,5]
my_set4 = set(my_list)
print(f'Convirtiendo una estructura de datos a set4 {my_set4}')

my_tuple = ("Hola","Hola","Hola",1)
my_set5 = set(my_tuple)
print(f'Convirtiendo una estructura de datos a set5 {my_set5}')

#Añadir elementos a un set el
my_set.add(1)
print(f'Añadir elementos al set1 {my_set}')

#Actualizar añadir multiples elementos a un set el
my_set.update([2,6,7])
print(f'Añadir multiples elementos al set1 {my_set}')

#Actualizar añadir multiples elementos a un set3
my_set3.update([2,6,7],{1,2,3,4,5,6,8,9})
print(f'Añadir elementos a un set el set3 {my_set3}')

#Eliminar un elemento del set3
my_set3.discard(2)
print(f'Eliminar un elemento del set3 {my_set3}')

#Eliminar un elemento existente del set3
my_set3.remove(3)
print(f'Eliminar un elemento existente del set3 {my_set3}')

#Eliminar elemento inexistente con discard genera error 
my_set3.discard(10)
print(f'Eliminar elemento inexistente con discard NO genera error del set3 {my_set3}')

#Eliminar elemento inexistente con discard genera error 
#my_set3.remove(10)
#print(f'Eliminar elemento inexistente con discard genera error del set3 {my_set3}')

#Eliminar elemento aleatoriodel set3
my_set3.pop()
print(f'Eliminar elemento aleatoriodel set3 {my_set3}')

#Limpiar el set
my_set3.clear()
print(f'Limpiar el set set3 {my_set3}')