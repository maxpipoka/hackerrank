"""
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example

s= '12:01:00PM'
Return '12:01:00'.

s= '12:01:00AM'
Return '00:01:00'.

Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

- string s: a time in  hour format

Returns
- string: the time in  hour format

Input Format
A single string  that represents a time in -hour clock format (i.e.:  or ).

Constraints

- All input times are valid

Sample Input 0
07:05:45PM

Sample Output 0
19:05:45
"""

#!/bin/python3

import os
import sys
#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    cadenaRecortada = s[:-2].split(":")
    horas = int(cadenaRecortada[0])
    minutos = cadenaRecortada[1]
    segundos = cadenaRecortada[2]
    
    if (s[-2] == "P") and (horas < 12):
        horas += 12
    elif (s[-2] == "A") and (horas == 12):
        horas = '00'
    elif(s[-2] == 'A') and (horas < 12):
        temporal = str(horas)
        horas = '0'+temporal

        
    impresion = str(horas) + ':' + str(minutos) + ':' + str(segundos)
    return impresion

if __name__ == '__main__':
#    f = open(os.environ['OUTPUT_PATH'], 'w')

#    s = input()
    s = '06:40:03AM'

    result = timeConversion(s)

#    f.write(result + '\n')

#    f.close()
print(result)
