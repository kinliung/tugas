import numpy as np
import matplotlib.pyplot as plt
import math
def func(expr, x):
    return eval(expr)

input_expr = input("Masukkan persamaan fungsi x = ")
a = eval(input("Masukkan nilai a : "))
b = eval(input("Masukkan nilai b : "))

x1=a
x2=b
y1=func(input_expr, x1)
y2=func(input_expr, x2)
if y1*y2>0:
  print("Tidak memiliki akar persamaan")
  exit
print("%2s %-6s %-6s %-6s %-7s %-6s %s" %('n', 'a', 'b', 'xn', 'f(a)', 'f(b)', 'f(xn)'))
for bisection in range(1,11):
  xh=(x1 + x2)/2
  yh=func(input_expr, xh)
  y1=func(input_expr, x1)
  y2 = func(input_expr, x2)
  if bisection == 9:
      xh2 = xh
  print('{0:2d} {1:.4f} {2:.4f} {3:.4f} {4:.4f} {5:.4f} {6:.4f}'.format((bisection), (x1), (x2), (xh), (y1), (y2), (yh)))
  if abs(y1)<1.0E-6:
    break
  elif yh*y1<0:
    x2=xh
  else:
    x1=xh


print("Akar persamaannya adalah = % 0.11f"% xh, "dan% 0.10f"% xh2)

x = np.linspace(a,b,100)
plt.plot(x,func(input_expr, x))
plt.grid()
plt.show()
