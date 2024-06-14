# Örnek: 2x + 3y maksimize et, x ve y tam sayıdır, x + 3y ≤ 13

# Hedef fonksiyon ve katsayıları
def objective_function(x, y):
    return 2 * x + 3 * y

# Kısıtların listesi
constraints = [
    lambda x, y: x + 3 * y <= 13
]

# Kısıtları ve tam sayı kısıtlarını sağlayan en iyi çözümü bul
best_solution = None
best_value = float('-inf')

for x in range(7):  # x için olası değerler (0'dan 6'ya kadar)
    for y in range(5):  # y için olası değerler (0'dan 4'e kadar)
        if all(constraint(x, y) for constraint in constraints):  # Tüm kısıtları kontrol et
            value = objective_function(x, y)
            if value > best_value:
                best_value = value
                best_solution = (x, y)

print("Optimal Çözüm:", best_solution)
print("Optimal Değer:", best_value)
