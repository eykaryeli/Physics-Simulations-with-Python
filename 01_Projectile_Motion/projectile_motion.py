v0 = 40 
g = 9.81
acilar = np.array([30,45,60])
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
for aci in acilar:
    radyan = np.radians(aci)
    vy0 = v0*np.sin(radyan)
    vx = v0*np.cos(radyan)

    t_ucus = 2*vy0/g
    t = np.linspace(0,t_ucus,100)

    x = vx*t
    y = vy0*t - 0.5*g*t**2

    h_max = y.max()
    tepe_idx = y.argmax()

    plt.plot(x,y,label=f"{aci} (h_max ={h_max:.1f}m )")
    plt.scatter(x[tepe_idx],h_max,color='red',zorder=4)

plt.title("Yörünge Karşılaştırması")
plt.xlabel("Mesafe (m)")
plt.ylabel("Yükseklik (m)")
plt.grid(True)
plt.legend()


plt.subplot(1, 2, 2)  


aci_45 = 45
rad_45 = np.radians(aci_45)

vx_45 = v0 * np.cos(rad_45)
vy0_45 = v0 * np.sin(rad_45)


t_ucus_45 = 2 * vy0_45 / g
t_45 = np.linspace(0, t_ucus_45, 100)


vy_t = vy0_45 - g * t_45


v_toplam = np.sqrt(vx_45**2 + vy_t**2)

# 5. Çizim ve Biçimlendirme
plt.plot(t_45, v_toplam, color='purple', label='Bileşke Hız v(t)')

plt.title("45° Atış İçin Hız - Zaman")
plt.xlabel("Zaman (s)")
plt.ylabel("Hız (m/s)")
plt.grid(True)
plt.legend()


plt.tight_layout()
plt.show()
