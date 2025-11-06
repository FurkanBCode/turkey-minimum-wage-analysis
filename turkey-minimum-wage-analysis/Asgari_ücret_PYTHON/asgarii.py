import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

folders = [
    "AsgariUcret_Analizi/Python/veri",
    "AsgariUcret_Analizi/Python/grafikler"
]

for f in folders:
    os.makedirs(f, exist_ok=True)

years = list(range(2015, 2026))
nominal = [1500, 1600, 1700, 1800, 1900, 2100, 2300, 2500, 2700, 2900, 3100]
real = [1500, 1550, 1580, 1600, 1620, 1650, 1680, 1700, 1720, 1750, 1780]

df = pd.DataFrame({
    'Yıl': years,
    'Nominal': nominal,
    'Real': real
})

df['Nominal_Yillik_Artis_%'] = df['Nominal'].pct_change() * 100
df['Real_Yillik_Artis_%'] = df['Real'].pct_change() * 100
df['Fark'] = df['Nominal'] - df['Real']

csv_path = "AsgariUcret_Analizi/Python/veri/AsgariUcret_2015_2025.csv"
df.to_csv(csv_path, index=False)

sns.set(style="whitegrid")

plt.figure(figsize=(10,5))
plt.plot(df['Yıl'], df['Nominal'], marker='o', label='Nominal')
plt.plot(df['Yıl'], df['Real'], marker='o', label='Real')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("AsgariUcret_Analizi/Python/grafikler/Nominal_Real_Grafik.png")
plt.close()

plt.figure(figsize=(10,5))
plt.plot(df['Yıl'], df['Nominal_Yillik_Artis_%'], marker='o', label='Nominal Yıllık Artış %')
plt.plot(df['Yıl'], df['Real_Yillik_Artis_%'], marker='o', label='Real Yıllık Artış %')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("AsgariUcret_Analizi/Python/grafikler/Yillik_Artis_Grafik.png")
plt.close()

plt.figure(figsize=(10,5))
sns.barplot(x='Yıl', y='Fark', data=df, palette="Oranges")
plt.tight_layout()
plt.savefig("AsgariUcret_Analizi/Python/grafikler/Fark_Grafik.png")
plt.close()
