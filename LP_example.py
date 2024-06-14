# Örnek: x + y ≤ 10, 2x + 3y ≤ 25, x ≥ 0, y ≥ 0, ve f(x, y) = 4x + 3y

# Hedef fonksiyon ve katsayıları
def objective_function(x, y):
    return 4 * x + 3 * y

# Kısıtların listesi
constraints = [
    lambda x, y: x + y <= 10,
    lambda x, y: 2 * x + 3 * y <= 25,
    lambda x, y: x >= 0,
    lambda x, y: y >= 0
]

# Kısıtları sağlayan en iyi çözümü bul
best_solution = None
best_value = float('-inf')

for x in range(11):  # x için olası değerler
    for y in range(11):  # y için olası değerler
        if all(constraint(x, y) for constraint in constraints):  # Tüm kısıtları kontrol et
            value = objective_function(x, y)
            if value > best_value:
                best_value = value
                best_solution = (x, y)

print("Optimal Çözüm:", best_solution)
print("Optimal Değer:", best_value)
