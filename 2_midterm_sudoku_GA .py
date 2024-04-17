import random

# Sudoku tahtasını oluşturmak için bir fonksiyon
def generate_individual():
    # Boş bir Sudoku tahtası oluştur
    individual = [[0]*9 for _ in range(9)]
    # Her satırı 1'den 9'a kadar rastgele rakamlarla doldur
    for i in range(9):
        individual[i] = random.sample(range(1, 10), 9)
    return individual

# Sudoku tahtasının uygunluk değerini hesaplamak için bir fonksiyon
def fitness(individual):
    # Uygunluk değeri başlangıçta sıfırdır
    fitness_score = 0
    # Her satırı kontrol et
    for row in individual:
        # Bir satırdaki benzersiz rakamların sayısını hesapla ve toplamdan çıkar
        fitness_score += 9 - len(set(row))
    # Toplam uygunluk değerini döndür
    return fitness_score

# Ana fonksiyon: Sudoku çözümünü bulmak
def solve_sudoku():
    # Başlangıç popülasyonunu oluştur
    population = [generate_individual() for _ in range(100)]
    generation = 0
    
    # Belirli bir duruma veya iterasyon sayısına ulaşana kadar döngüyü çalıştır
    while generation < 1000:
        # Her bir bireyin uygunluk değerini hesapla
        fitness_values = [fitness(individual) for individual in population]
        # Eğer en iyi bireyin uygunluk değeri 0 ise Sudoku çözülmüş demektir
        if 0 in fitness_values:
            print("Sudoku çözüldü:")
            print_board(population[fitness_values.index(0)])
            return
        # Yeni nesil için ebeveynler seç
        parent1 = random.choice(population)
        parent2 = random.choice(population)
        # Yeni bir çocuk oluştur
        child = crossover(parent1, parent2)
        # Yeni nesle mutasyon uygula
        mutate(child)
        # Yeni nesli popülasyona ekle
        population.append(child)
        # Yeniden popülasyonu değerlendir
        generation += 1
    
    # Belirli bir iterasyon sayısına ulaşıldığında veya Sudoku çözülmediğinde çözümü bulamadık
    print("Sudoku çözülemedi.")

# Sudoku tahtasını yazdırmak için bir fonksiyon
def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

# Sudoku tahtasında çaprazlama işlemi gerçekleştir
def crossover(parent1, parent2):
    # Basitçe ebeveynlerden rastgele bir satırı ve sütunu seçerek çaprazlama yap
    child = parent1[:]
    row = random.randint(0, 8)
    col = random.randint(0, 8)
    child[row][col:] = parent2[row][col:]
    return child

# Sudoku tahtasında mutasyon işlemi gerçekleştir
def mutate(individual):
    # Basitçe bir hücrenin değerini rastgele bir rakamla değiştir
    row = random.randint(0, 8)
    col = random.randint(0, 8)
    individual[row][col] = random.randint(1, 9)

# Sudoku bulmacasını çözmek için solve_sudoku fonksiyonunu çağırın
solve_sudoku()
