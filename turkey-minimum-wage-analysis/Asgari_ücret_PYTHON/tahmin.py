import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# === GERÇEK VERİLER ===
years = np.array(range(2015, 2026))
asgari_net = np.array([1000, 1300, 1404, 1603, 2020, 2324, 2825, 4253, 5500, 8506, 22102])  # TL
tufe = np.array([8.2, 8.5, 11.9, 20.3, 11.8, 14.6, 36.1, 64.3, 53.0, 45.0, 29.0])  # %

# === GELECEK YILLAR ===
future_years = np.array(range(2026, 2031))

# Gerçekçi TÜFE tahminleri (tahminsel kaynaklara göre)
tufe_future = np.array([30, 25, 22, 20, 18])  # 2026–2030 TÜFE tahmini

# Gelecek yıllar için net asgari ücret tahmini
net_pred = [asgari_net[-1]]
for oran in tufe_future:
    yeni = net_pred[-1] * (1 + oran / 100)
    net_pred.append(yeni)
net_pred = np.array(net_pred[1:])

# Gerçek değer tahmini
real_future = net_pred / (1 + tufe_future / 100)

# === TÜM VERİYİ BİRLEŞTİR ===
all_years = np.concatenate([years, future_years])
all_net = np.concatenate([asgari_net, net_pred])
all_tufe = np.concatenate([tufe, tufe_future])
real_value = asgari_net / (1 + tufe / 100)
all_real = np.concatenate([real_value, real_future])

# === GRAFİK ===
plt.figure(figsize=(12,6))

plt.plot(years, asgari_net, marker='o', color='blue', label='Net (Gerçek)')
plt.plot(future_years, net_pred, marker='o', linestyle='--', color='blue', label='Net (Tahmin)')

plt.plot(years, real_value, marker='s', color='green', label='Gerçek Değer')
plt.plot(future_years, real_future, marker='s', linestyle='--', color='green', label='Gerçek Değer (Tahmin)')

plt.plot(years, tufe*400, linestyle=':', marker='x', color='orange', label='TÜFE x400')
plt.plot(future_years, tufe_future*400, linestyle=':', marker='x', color='orange', label='TÜFE x400 (Tahmin)')

plt.axvline(x=2025, color='gray', linestyle='--')
plt.text(2025.2, all_net[-1]*0.9, "Tahmin Başlangıcı", color='red', fontsize=10)

plt.title("2015–2030 Net Asgari Ücret & TÜFE & Gerçek Değer Tahmini", fontsize=13)
plt.xlabel("Yıl")
plt.ylabel("TL (TÜFE x400 ölçeğinde)")
plt.grid(True)
plt.gca().yaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,.0f} TL'))

for x, y in zip(all_years, all_net):
    plt.text(x, y+300, f"{int(y):,}", ha='center', fontsize=8, color='blue')
for x, y in zip(all_years, all_real):
    plt.text(x, y-500, f"{int(y):,}", ha='center', fontsize=8, color='green')

plt.legend()
plt.tight_layout()
plt.show()

# === TABLO ===
df = pd.DataFrame({
    "Yıl": all_years,
    "TÜFE (%)": all_tufe,
    "Net Asgari Ücret (TL)": all_net.astype(int),
    "Gerçek Değer (TL)": all_real.astype(int)
})
print(df.tail(10))
