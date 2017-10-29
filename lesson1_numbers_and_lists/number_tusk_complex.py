#1.Дано комплексное число Z, вида Z=x+jy, где x и y - вещественные числа, а j - мнимая единица. 
#Необходимо представить данное число в полярной системе координат, которое определяется r - длинной вектора z, и phi - углом поворота вектора Z против часовой стрелки.

import math
from math import pi 

z = complex (input())
y=z.imag
x=z.real 
if x !=0:
    xmz=0.5-x/(2*abs(x)) # равен 0 при x>0 и 1 при x<0
if y!=0:
    ymz=pi*y/abs(y) # равен pi при y>0 и -pi при x<0
print (math.sqrt(x**2+y**2))    
if x==0:
    phi = ymz/2    
elif y==0:
    phi = xmz*pi
else:
    phi = (xmz*ymz + math.atan(y/x))

pmz = 180-180*phi/abs(phi) # равен 0 при phi>0 и 360 при phi<0
print (180*phi/pi+pmz) #перевод в градусы. 





