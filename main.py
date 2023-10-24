import math
import numpy as np
from matplotlib import pyplot as plt

t0 = 0
t1 = 0.00038 * 10 ** 9
t2 = (10.3 + 0.00038) * 10 ** 9
t3 = (11.2 + 0.00038) * 10 ** 9

a0 = 0
a1 = ((t2 ** 3) * t3 ** 2 - (t2 ** 2) * (t3 ** 3) + 2 * (t1 ** 2) * (t3 ** 3) + 3 * (t1 ** 3) * (t2 ** 2) - 2 * (
        t1 ** 3) * (t3 ** 2) - 3 * (t1 ** 2) * (t2 ** 3)) / (t1 * t2 * t3 * (t1 - t2) * (t1 - t3) * (t2 - t3))
a2 = -(t3 * (t2 ** 3) - t2 * (t3 ** 3) + 2 * t1 * (t3 ** 3) + 3 * t2 * (t1 ** 3) - 2 * t3 * (t1 ** 3) - 3 * t1 * (
        t2 ** 3)) / (t1 * t2 * t3 * (t1 - t2) * (t1 - t3) * (t2 - t3))
a3 = (t3 * (t2 ** 2) - t2 * (t3 ** 2) + 2 * t1 * (t3 ** 2) + 3 * t2 * (t1 ** 2) - 2 * t3 * (t1 ** 2) - 3 * t1 * (
        t2 ** 2)) / (t1 * t2 * t3 * (t1 - t2) * (t1 - t3) * (t2 - t3))
print(a0)
print(a1)
print(a2)
print(a3)


# a0 = 0
# a1 = 2.63176824127625e-6
# a2 = -4.98150792508823e-16
# a3 = 2.34995037389168e-26
#
# print(a0)
# print(a1)
# print(a2)
# print(a3)

# P = 0 + (2.63176824127625e-6) * x + (-4.98150792508823e-16) * (x^2) + (2.34995037389168e-26) * (x^3)
#
def PolyCoefficients(x, coeffs):
    o = len(coeffs)
    y = 0
    for i in range(o):
        y += coeffs[i] * x ** i
    return y


# a0 + a1*t4 + a2 * (t4**2) + a3 * (t4**3)  = 4;

p = ((3 * a3 * a1) - (a2 ** 2)) / (3 * (a3 ** 2))
q = ((2 * (a2 ** 3)) - 9 * a3 * a2 * a1 + 27 * (a3 ** 2) * (-4)) / (27 * (a3 ** 3))

D = ((p / 3) ** 3) + ((q / 2) ** 2)

if D < 0:
    if q < 0:
        phi = math.atan(math.sqrt(-D) / -(q / 2))
    elif q > 0:
        phi = math.atan(math.sqrt(-D) / -(q / 2)) + math.pi
    elif q == 0:
        phi = math.pi / 2
    y1 = 2 * math.sqrt(-(p / 3)) * math.cos(phi / 3)
    y2 = 2 * math.sqrt(-(p / 3)) * math.cos((phi / 3) + (2 * math.pi) / 3)
    y3 = 2 * math.sqrt(-(p / 3)) * math.cos((phi / 3) + (4 * math.pi) / 3)

    x1 = y1 - a2 / (3 * a3)
    x2 = y2 - a2 / (3 * a3)
    x3 = y3 - a2 / (3 * a3)
    print("D < 0")
    print(x1, x2, x3)

if D > 0:
    y1 = (((-(q / 2)) + math.sqrt(D)) ** (1 / 3)) + (((-(q / 2)) - math.sqrt(D)) ** (1 / 3))

    y2 = (-1 / 2) * ((((-(q / 2)) + math.sqrt(D)) ** (1 / 3)) + (((-(q / 2)) - math.sqrt(D)) ** (1 / 3))) + complex(0,
                                                                                                                    math.sqrt(
                                                                                                                        3) / 2) * (
                     (((-(q / 2)) + math.sqrt(D)) ** (1 / 3)) + (((-(q / 2)) - math.sqrt(D)) ** (1 / 3)))

    y3 = (-1 / 2) * ((((-(q / 2)) + math.sqrt(D)) ** (1 / 3)) + (((-(q / 2)) - math.sqrt(D)) ** (1 / 3))) - complex(0,
                                                                                                                    math.sqrt(
                                                                                                                        3) / 2) * (
                     (((-(q / 2)) + math.sqrt(D)) ** (1 / 3)) + (((-(q / 2)) - math.sqrt(D)) ** (1 / 3)))

    x1 = y1 - a2 / (3 * a3)
    x2 = y2 - a2 / (3 * a3)
    x3 = y3 - a2 / (3 * a3)
    print("D > 0")
    print(x1, x2, x3)

if D == 0:
    if q == 0 and p == 0:
        y1 = 0
        x1 = - a2 / (3 * a3)
        flag = 4
        print("D = 0; q = 0; p = 0")
        print(x1)
    else:
        y1 = 2 * (-q / 2) ** (1 / 3)
        y2 = -(-q / 2) ** (1 / 3)
        x1 = y1 - a2 / (3 * a3)
        x2 = y2 - a2 / (3 * a3)
        print("D = 0")
        print(x1, x2)
print(t3)
# plt.plot(t0, 0, 'ro')
# plt.plot(t1, 1, 'ro')
# plt.plot(t2, 2, 'ro')
# plt.plot(t3, 3, 'ro')
# plt.plot(x1, 4, 'go')
x = np.linspace(-100*10**9, 100*10**9, 1000)
coeffs = [a0, a1, a2, a3]
plt.plot(x, PolyCoefficients(x, coeffs), 'b')
plt.grid()
plt.show()
