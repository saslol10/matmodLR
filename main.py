import math
from matplotlib import pyplot as plt

t0 = 0
t1 = 380000
t2 = 10.3 * (10 ** 9) + 380000
t3 = 11.2 * (10 ** 9) + 380000

a0 = 0
a1 = ((t2 ** 3) * t3 ** 2 - (t2 ** 2) * (t3 ** 3) + 2 * (t1 ** 2) * (t3 ** 3) + 3 * (t1 ** 3) * (t2 ** 2) - 2 * (
        t1 ** 3) * (t3 ** 2) - 3 * (t1 ** 2) * (t2 ** 3)) / (t1 * t2 * t3 * (t1 - t2) * (t1 - t3) * (t2 - t3))
a2 = -(t3 * (t2 ** 3) - t2 * (t3 ** 3) + 2 * t1 * (t3 ** 3) + 3 * t2 * (t1 ** 3) - 2 * t3 * (t1 ** 3) - 3 * t1 * (
        t2 ** 3)) / (t1 * t2 * t3 * (t1 - t2) * (t1 - t3) * (t2 - t3))
a3 = (t3 * (t2 ** 2) - t2 * (t3 ** 2) + 2 * t1 * (t3 ** 2) + 3 * t2 * (t1 ** 2) - 2 * t3 * (t1 ** 2) - 3 * t1 * (
        t2 ** 2)) / (t1 * t2 * t3 * (t1 - t2) * (t1 - t3) * (t2 - t3))

# a0 + a1*t4 + a2 * (t4**2) + a3 * (t4**3)  = 4;

p = ((3 * a3 * a1) - (a2 ** 2)) / (3 * (a3 ** 2))
q = ((2 * (a2 ** 3)) - 9 * a3 * a2 * a1 + 27 * (a3 ** 2) * (-4)) / (27 * (a3 ** 3))

D = ((p / 3) ** 3) + ((q / 2) ** 2)

flag = 0

if D < 0:
    if q < 0:
        phi = math.atan(math.sqrt(-D) / (q / 2))
    elif q > 0:
        phi = math.atan(math.sqrt(-D) / (q / 2)) + math.pi
    elif q == 0:
        phi = math.pi / 2
    y1 = 2 * math.sqrt(-(p / 3)) * math.cos(phi / 3)
    y2 = 2 * math.sqrt(-(p / 3)) * math.cos((phi / 3) + (2 * math.pi) / 3)
    y3 = 2 * math.sqrt(-(p / 3)) * math.cos((phi / 3) + (4 * math.pi) / 3)

    x1 = y1 - a2/(3*a3)
    x2 = y2 - a2/(3*a3)
    x3 = y3 - a2/(3*a3)
    print("Q < 0")
    print(x1, x2, x3)
    flag = 1
#    plt.plot([t0, t1, t2, t3, max(t3, x1, x2, x3)], [0, 1, 2, 3, 4])
#    plt.show()

if D > 0:
    y1 = (((-(q/2)) + math.sqrt(D)) ** (1 / 3)) + (((-(q / 2)) - math.sqrt(D)) ** (1 / 3))

    y2 = (-1/2) * ((((-(q/2)) + math.sqrt(D)) ** (1 / 3)) + (((-(q / 2)) - math.sqrt(D)) ** (1 / 3))) + complex(0, math.sqrt(3) / 2) * ((((-(q / 2)) + math.sqrt(D)) ** (1 / 3)) + (((-(q / 2)) - math.sqrt(D)) ** (1 / 3)))

    y3 = (-1/2) * ((((-(q/2)) + math.sqrt(D)) ** (1 / 3)) + (((-(q / 2)) - math.sqrt(D)) ** (1 / 3))) - complex(0, math.sqrt(3) / 2) * ((((-(q / 2)) + math.sqrt(D)) ** (1 / 3)) + (((-(q / 2)) - math.sqrt(D)) ** (1 / 3)))

    x1 = y1 - a2 / (3 * a3)
    x2 = y2 - a2 / (3 * a3)
    x3 = y3 - a2 / (3 * a3)
    print("Q > 0")
    print(x1, x2, x3)
    flag = 2
if D == 0:
    if q == 0 and p == 0:
        y1 = 0
        x1 = - a2 / (3 * a3)
        flag = 4
        print("Q = 0; q = 0; p = 0")
        print(x1)
    else:
        y1 = 2 * (-q/2) ** (1/3)
        y2 = -(-q/2) ** (1/3)
        x1 = y1 - a2 / (3 * a3)
        x2 = y2 - a2 / (3 * a3)
        print("Q = 0")
        print(x1, x2)
        flag = 3

