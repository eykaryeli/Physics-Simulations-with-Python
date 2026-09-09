import numpy as np
import matplotlib.pyplot as plt

g = 9.81
rad = np.radians(10)
ip = np.array([0.5,1.0,2.0])
t = np.linspace(0,5,200)
plt.figure(figsize = (12,5))

plt.subplot(1,2,1)
for L in ip:
    w = np.sqrt(g / L)
    theta = rad * np.cos(w * t)
    plt.plot(t, np.degrees(theta) , label = f"L = {L}m")
plt.xlabel("Zaman(s)")
plt.ylabel("Açı(Derece)")
plt.grid(True)
plt.legend()

plt.subplot(1,2,2)
ldizi = np.linspace(0.2,3.0,100)
wdizi = np.sqrt(g / ldizi)
plt.plot(wdizi,ldizi)
plt.xlabel("Açısal Frekans")
plt.ylabel("İp Uzunluğu")
plt.grid(True)

plt.show

   
    

