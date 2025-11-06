import matplotlib.pyplot as plt

# 2015-2025 Yıllar
yillar = list(range(2015, 2026))

# Nominal net asgari ücretler (TL)
nominal = [
    1000.54, 1300.99, 1404, 1603, 2020.59,
    2324.7, 2825.9, 5500.35, 11402.32, 17002, 22104.67
]

# Yıllık TÜFE oranları (%)
tufe_yillik = [
    8.8, 8.53, 11.92, 20.3, 11.84,
    14.6, 36.08, 64.27, 64.77, 44.38, 32.87
]

# Reel alım gücü: nominal / (1 + TÜFE/100)
alim_gucu = [nominal[i] / (1 + tufe_yillik[i]/100) for i in range(len(yillar))]

# Grafik ayarları
plt.figure(figsize=(14,6))
bar_width = 0.2
gap = 0.05
x = range(len(yillar))

# Barlar
bars_nominal = plt.bar([p - bar_width/2 - gap for p in x], nominal, width=bar_width, label='Nominal Asgari Ücret', color='skyblue')
bars_alim = plt.bar([p + bar_width/2 + gap for p in x], alim_gucu, width=bar_width, label='Gerçek Alım Gücü (TÜFE Bazlı)', color='orange')

# Bar üstüne değer yaz (etiket kutusu ve dikine)
for i, (bar_nom, bar_real) in enumerate(zip(bars_nominal, bars_alim)):
    # Etiket kutusu ayarları
    bbox_props = dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=0.7, alpha=0.9)
    
    # 2015-2019 için biraz yukarı kaydır
    if yillar[i] <= 2019:
        plt.text(bar_nom.get_x() + bar_nom.get_width()/2, nominal[i]*1.2, f'{nominal[i]:,.0f} TL', 
                 ha='center', va='bottom', fontsize=9, fontweight='bold', rotation=90, bbox=bbox_props)
        plt.text(bar_real.get_x() + bar_real.get_width()/2, alim_gucu[i]*1.25, f'{alim_gucu[i]:,.0f} TL', 
                 ha='center', va='bottom', fontsize=9, fontweight='bold', rotation=90, bbox=bbox_props)
    else:  # 2020-2025 normal üstüne yaz
        plt.text(bar_nom.get_x() + bar_nom.get_width()/2, nominal[i]*1.1, f'{nominal[i]:,.0f} TL', 
                 ha='center', va='bottom', fontsize=9, fontweight='bold', rotation=90, bbox=bbox_props)
        plt.text(bar_real.get_x() + bar_real.get_width()/2, alim_gucu[i]*1.15, f'{alim_gucu[i]:,.0f} TL', 
                 ha='center', va='bottom', fontsize=9, fontweight='bold', rotation=90, bbox=bbox_props)

# X ekseni ve etiketler
plt.xticks(x, yillar)
plt.ylabel('TL / Reel Alım Gücü')
plt.title('2015–2025: Türkiye Asgari Ücret ve Reel Alım Gücü (TÜFE Bazlı)')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
