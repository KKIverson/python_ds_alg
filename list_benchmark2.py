from timeit import Timer
import matplotlib.pyplot as plt


popzero = Timer("x.pop(0)", "from __main__ import x")
popend = Timer("x.pop()", "from __main__ import x")
print("pop(0)   pop()")
pzy = []
pty = []
xlabel = list(range(10000, 1000001, 10000))

for i in range(10000, 1000001, 10000):
    x = list(range(i))
    pt = popend.timeit(number=1000)
    x = list(range(i))
    pz = popzero.timeit(number=1000)
    print("%15.5f, %15.5f" %(pt, pz))
    pzy.append(pz)
    pty.append(pt)

plt.plot(xlabel, pzy)
plt.plot(xlabel, pty)
plt.show()