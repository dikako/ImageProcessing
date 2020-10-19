import numpy 
from PIL import Image

x = Image.open("image/image.jpeg")
y = numpy.asarray(x)
print(y)
print(y.shape)
kolom, baris, dimensi = y.shape
m = max(kolom, baris)
z = numpy.zeros((m, m, 3), dtype = numpy.uint8)

for i in range(m - 340, m):
  for j in range(m):
    z[i, j] = [0, 0, 0]

for i in range(90):
  for j in range(m):
    z[i, j] = [170, 150, 130]

for i in range(90, m - 340):
  for j in range(m):
    z[i, j] = y[i - 90, j]

gambar_square = Image.fromarray(z)
gambar_square.save("image_canges/img_square.jpeg")

gambar_awal = Image.open("image_canges/img_square.jpeg")
matriks_awal = numpy.asarray(gambar_awal)

p = 2; q = 3; iterasi = 1
matriks_enkrip = numpy.zeros(matriks_awal.shape, dtype = numpy.uint8)

for i in range(m):
  for j in range(m):
    x0 = i; y0 = j
    for k in range(iterasi):
      x = (x0 + p*y0)%m
      y = (q*x0 + y0*(p*q + 1))%m
      x0 = x; y0 = y
      matriks_enkrip [x0, y0] = matriks_awal[i, j]
back1st = Image.fromarray(matriks_enkrip)
back1st.save("image_canges/img_encrypt.jpeg")

gambar_enkrip = Image.open("image_canges/img_encrypt.jpeg")
matriks_enkrip = numpy.asarray(gambar_enkrip)
matriks_dekryp = numpy.zeros(matriks_enkrip.shape, dtype = numpy.uint8)

for i in range(m):
  for j in range(m):
    x0 = i; y0 = i
    for k in range(iterasi):
      x = (x0*(p*q+1) - p*y0)%m
      y = (-q*x0 + y0)%m
      x0 = x; y0 = y
    matriks_dekryp [x0, y0] = matriks_enkrip [i, j]
back2end = Image.fromarray(matriks_dekryp)
back2end.save("image_canges/img_decrypt.jpeg")





