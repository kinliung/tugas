import numpy as np
import matplotlib.pyplot as plt

def fungsi(x):
    return x**3-3*x-20
def TurunanFungsi(x):
    return 3*(x**2)-3
def newtonRaphson(x):
    h = fungsi(x) / TurunanFungsi(x)
    x1 = x - h
    i = 1
    while (i<n):
        x = x1
        h = fungsi(x) / TurunanFungsi(x)
        x1 = x - h
        i += 1
        if (abs((x1 - x)/x1) < e):
          break
     else:
        print('Sudah mencapai iterasi maksimun')
    print('Akar Persamaannya :',
          '%.4f' % x, 'pada iterasi ke-', i, 'dengan ketelitian', abs((x1 - x)/x1))

x0 = float(input('Nilai X0 : '))
e = float(input('Masukkan nilai ketelitian/error : '))
n = int(input('Masukkan iterasi maksimum : '))
newtonRaphson(x0)

x = np.linspace(x0-5,x0+5,100)
plt.plot(x, fungsi(x))
plt.grid()
plt.show()
