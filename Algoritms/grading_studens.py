''' La Universidad Hackerranks tiene la siguiente politica de graduacion:
- Cada estudiante recibe un grado en el rango de 0 a 100 inglusive.
- Todo grado menor a 40 es un grado fallido.

Sam es profesor en la universidad y le gusta redondear el grado de los estudiantes de acuerdo a estas reglas:
- Si la diferencia entre el GRADO y el siguiente multiplo de 5 es mejor a 3, se redondea el grado para arriba hasta el siguiente multiplo de 5.
- Si el valor del grado es menor a 38, no ocurre redondeo ya que el resultado seguirá siendo grado fallido.

Ejemplos:
grado = 84, se redondea a 85 (85 - 84 es menor a 3)
grado = 29 no se redondea (el resultado es menor a 40)
grado = 57 no se redondea (60 - 57 es 3 o mayor)

Dado el valor inicial del grado para cada uno de los N alumnos de Sam, escriba el codito para automatizar el proceso de redondeo.

Descripcion de la funcion
Complete la funcion gradingStrudents en el editor a continuacion.

gradingStudents tiene los siguientes parametros:
- int grades[n]: el grado antes del redondeo

Retorna
- int[n]: el grado despues del redondeo segun corresponda.

Formato de entrada
La primer linea contiene un numero entero, N, el numero de estudiantes.
Cada linea i de el n en las lineas subsecuentes contienen un entero simple, grades[i].

Restricciones
- 1 =< n <= 60
- 0 <= grades[i] <= 100

Ejemplo de entrada 0
4
73
67
38
33

Ejemplo de salida 0
-
75
67
40
33

'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#


def gradingStudents(grades):
    # Write your code here
    count_grades = grades[0]
    grades_rounded = []
    multiplos5 = []
    
    x = 0
    for x in range(20):
        multiplos5.append(5 * x)

    i = 0
    while i != (count_grades + 1):
        grade_round = grades[i +1]



        i++


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
