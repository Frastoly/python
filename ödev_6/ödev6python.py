import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

# 0-1000 arası rastgele x ve y koordinatları üret
x = np.random.rand(1000) * 1000
y = np.random.rand(1000) * 1000

# Koordinatları DataFrame'e dönüştür
df = pd.DataFrame({'x': x, 'y': y})

# DataFrame'i Excel dosyası olarak kaydet
df.to_excel('koordinatlar.xlsx', index=False)

# Excel dosyasını oku
df = pd.read_excel('koordinatlar.xlsx')

# Izgara boyutu
grid_size = 50

# Izgara sayısı
grid_count = int(1000 / grid_size)

# Her ızgaraya rastgele renk ata
colors = np.random.rand(grid_count, grid_count, 3)

# Grafik oluştur
plt.figure(figsize=(10, 10))

for i in range(grid_count):
    for j in range(grid_count):
        # Izgara sınırları
        x_min = i * grid_size
        x_max = (i + 1) * grid_size
        y_min = j * grid_size
        y_max = (j + 1) * grid_size

        # Izgaraya ait noktaları filtrele
        grid_points = df[(df['x'] >= x_min) & (df['x'] < x_max) & (df['y'] >= y_min) & (df['y'] < y_max)]

        # Noktaları çizdir
        plt.scatter(grid_points['x'], grid_points['y'], c=colors[i, j], marker='o')

# Izgara çizgileri ekle
plt.grid(True, linestyle='-', linewidth=0.5)

# Grafik başlığı
plt.title('Rastgele Koordinatlar ve Izgara Renklendirme')

# Grafiği göster
plt.show()
