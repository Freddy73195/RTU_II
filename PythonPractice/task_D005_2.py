import math as m

k = 1
x = 1
a = 1
y = 1
q = m.sqrt(m.fabs(m.cos(pow(x, 2) + m.radians(44)) + a * pow(m.sin(k * y), 2))) - 0.6 * pow(y, 3) + m.log2(8) / (4 * a)
print(q)

x = 1
y = 1
b = m.e**(m.fabs(4*y - 0.5)) + ((x ** (1. / 3.))/ (1 + m.log(2*x, m.e)))
print(b)
