import math
x1 = int(input('insira a coordenada x1:'))
y1 = int(input('insira a coordenada y1:'))
x2 = int(input('insira a coordenada x2:'))
y2 = int(input('insira a coordenada y2:'))

dxy = math.sqrt ((x1-x2)**2 + (y1-y2)**2)

if dxy >= 10:
    print ('longe')
else:
    print ('perto')
