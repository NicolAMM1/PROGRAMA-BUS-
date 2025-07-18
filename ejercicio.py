
cursos =("Matematica",["Ana", "Luis","Carla",],[17,15,18]),("Historia", ["Pedro","Lucia","Marco"],[14,16,15]),("Programacion",["Elena","Raul","Sofia"],[20,19,18])

for curso in cursos: 
    nombre_curso, estudiantes, notas= curso  
    print (f"\n 📒Curso: {nombre_curso}")
    
    suma = 0
    for i in range(len(estudiantes)):
        estudiante=estudiantes[i].upper()
        nota = notas[1]
        print(f"Estudiante:{estudiante}, Nota: {nota}")
        suma+=nota
        
    promedio =suma/len(estudiantes)
    print(f"📊 promedio del curso: {promedio:.2f}")