import numpy as np 
import matplotlib.pyplot as plt
plt.figure(figsize = (12,5))
m = 1 
l = 1 
g = 9.81
theta_max = 5
rad = np.radians(theta_max)
t = np.linspace(0,5,200)

w = np.sqrt(g / l)
theta = rad * np.cos (w * t)
h = l * (1 - np.cos(theta))
v = - l * rad * w * np.sin(w * t)
Ep = m * g * h
Ek = 0.5 * m * v**2
Et = Ek + Ep

plt.subplot(1,2,1)
plt.plot(t,Et,label = "Toplam Enerji")
plt.plot(t, Ep , label = "Potansiyel Enerji")
plt.plot(t, Ek, label = "Kinetik Enerji")
plt.xlabel("Zaman (s)")
plt.ylabel("Enerji (J)")
plt.legend()
plt.grid(True)
plt.subplot(1,2,2)
plt.plot(np.degrees(theta),Ep, label = "Potansiyel Enerji")
plt.plot(np.degrees(theta),Et, label = "Toplam Enerji")
plt.plot(np.degrees(theta),Ek, label = "Kinetik Enerji")
plt.xlabel("Açı")
plt.ylabel("Enerji")
plt.legend()
plt.grid(True)
plt.tight_layout()
