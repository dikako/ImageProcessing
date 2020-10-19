import numpy
from PIL import Image


gambar_enkrip = Image.open("image/image.jpeg")
matriks_enkrip = numpy.asarray(gambar_enkrip)
matriks_dekrip = numpy.zeros(matriks_enkrip.shape, dtype = numpy.uint8)

x = gambar_enkrip
y = numpy.asarray(x)
kolom, baris, dimensi = y.shape 
m = max(kolom,baris)

p = 2   
q = 3
iterasi = 1

for i in range(m):
    for j in range(m):
        x0 = i
        y0 = j
        for k in range(iterasi):
            x = (x0* (p*q+1) - p*y0)%m
            y = (-q*x0 + y0)%m
            x0 = x
            y0 = y
        matriks_dekrip [x0,y0] = matriks_enkrip[i,j]
back2end = Image.fromarray(matriks_dekrip)
back2end.save("image_changes/doraeamon_encrypted")

