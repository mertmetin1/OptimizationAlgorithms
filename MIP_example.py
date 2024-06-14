"""

Matematiksel Modelleme:

    x1,x2,x3x1​,x2​,x3​: Sırasıyla Ürün A, Ürün B ve Ürün C'nin günlük satış miktarları.
    p1,p2,p3p1​,p2​,p3​: Sırasıyla Ürün A, Ürün B ve Ürün C'nin birim fiyatları.
    d1,d2,d3d1​,d2​,d3​: Sırasıyla Ürün A, Ürün B ve Ürün C'nin günlük talep miktarları.
    s1,s2,s3s1​,s2​,s3​: Sırasıyla Ürün A, Ürün B ve Ürün C'nin günlük stok miktarları.

Hedef Fonksiyon:
Maximize ∑i=13pi⋅xi
Maximize i=1∑3​pi​⋅xi​

Kısıtlar:

    Talep miktarlarını aşmamak:

xi≤di for i=1,2,3
xi​≤di​ for i=1,2,3

    Stok miktarlarını aşmamak:

xi≤si for i=1,2,3
xi​≤si​ for i=1,2,3

"""


# Ürünler ve ilişkili veriler
products = ['Ürün A', 'Ürün B', 'Ürün C']
demand = [50, 30, 40]  # Günlük talep miktarı
stock = [60, 40, 70]   # Günlük stok miktarı
prices = [5, 8, 7]  # Ürün başına fiyat

# Model oluşturma
best_solution = None
best_revenue = 0

# Tüm kombinasyonları dene ve en iyi çözümü bul
for i in range(stock[0] + 1):  # Ürün A için mümkün stok miktarları
    for j in range(stock[1] + 1):  # Ürün B için mümkün stok miktarları
        for k in range(stock[2] + 1):  # Ürün C için mümkün stok miktarları
            if i * prices[0] + j * prices[1] + k * prices[2] > best_revenue:
                if i <= demand[0] and j <= demand[1] and k <= demand[2]:
                    best_revenue = i * prices[0] + j * prices[1] + k * prices[2]
                    best_solution = [i, j, k]

print('En İyi Çözüm:')
for i in range(len(products)):
    print(products[i] + ' Satış Miktarı:', best_solution[i])
print('Toplam Gelir:', best_revenue)
