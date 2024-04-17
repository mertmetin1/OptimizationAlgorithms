def generate_combinations(n):
    combinations = []

    def backtrack(combination):
        if len(combination) == n:
            combinations.append(combination)
            return
        backtrack(combination + [0])
        backtrack(combination + [1])

    backtrack([])
    return combinations

# Örnek binary sayı
x = '000000'

# Binary sayının uzunluğu, yani basamak sayısı
n = len(x)

# Tüm kombinasyonları oluştur
all_combinations = generate_combinations(n)

# Kombinasyonların sayısı
total_combinations = len(all_combinations)

print("Toplam kombinasyon sayısı:", total_combinations)
print("Tüm kombinasyonlar:")
for combination in all_combinations:
    print(combination)
