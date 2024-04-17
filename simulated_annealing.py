import math
import random

# Çıktı dosyası
output_file = "simulated_annealing_output.txt"

# Başlangıç noktası seçimi
def initial_solution(file):
    # Rastgele başlangıç noktası seçimi [-10, 10] aralığında yapılır
    file.write("initial solution: {}\n".format([random.uniform(-10, 10), random.uniform(-10, 10)]))
    return [random.uniform(-10, 10), random.uniform(-10, 10)]

# (Objective Function)Enerji fonksiyonu (minimize etmeye çalıştığımız fonksiyon)
def energy(solution, file):
    # Parabol fonksiyonunu kullanıyoruz, bu nedenle enerjiyi bu fonksiyon hesaplar
    x, y = solution
    file.write("energy of {}: {}\n".format(solution, (x**2 + y**2)))
    return (x**2 + y**2)  # Parabol fonksiyonu

# Komşu çözüm seçimi(Random Neighbourhood Selecting(Random Walk))
def neighbor(solution, step_size, file):
    # Mevcut çözümden belirli bir adım boyutunda rastgele bir komşu çözüm seçimi
    x, y = solution
    new_x = x + random.uniform(-step_size, step_size)
    new_y = y + random.uniform(-step_size, step_size)
    file.write("random closest neighbour of {} is : {}\n".format(solution, [new_x,new_y]))
    return [new_x, new_y]

# Kabul edilebilirlik kriteri
def acceptance_probability(energy_old, energy_new, temperature, file):
    # Yeni enerji, eski enerjiden daha düşükse her zaman kabul edilir
    if energy_new < energy_old:
        file.write("energy_new < energy_old : return 1\n")
        return 1
    # Aksi takdirde, belirli bir olasılıkla kabul edilir
    else:
        file.write("energy_new < energy_old : return (daha kötü çözümün seçilme olasılığı) {}\n".format(math.exp((energy_old - energy_new) / temperature)))
        return math.exp((energy_old - energy_new) / temperature)

# Simulated Annealing algoritması
def simulated_annealing(initial_solution, energy, neighbor, acceptance_probability, initial_temperature, cooling_rate):
    i=0
    with open(output_file, "a") as file:
        current_solution = initial_solution(file)
        file.write("{} current solution = {}\n".format(i, current_solution))
        current_energy = energy(current_solution, file)
        file.write("{} current energy = {}\n".format(i, current_energy))
        best_solution = current_solution
        file.write("{} best solution = {}\n".format(i, current_solution))
        best_energy = current_energy
        file.write("{} best energy = {}\n".format(i, current_energy))
        temperature = initial_temperature
        file.write("{} temperature = {}\n".format(i, initial_temperature))
        # Sıcaklık belirli bir eşiğin altına düşene kadar devam eder

        while temperature > 0.1:
            i+=1
            # Yeni bir komşu çözüm seçilir
            new_solution = neighbor(current_solution, 0.1, file)
            new_energy = energy(new_solution, file)
            # Kabul edilebilirlik kriterine göre çözümün kabul edilip edilmeyeceği belirlenir
            if acceptance_probability(current_energy, new_energy, temperature, file) > random.random():
                current_solution = new_solution
                file.write("{} current solution = {}\n".format(i, current_solution))
                current_energy = new_energy
                file.write("{} current energy = {}\n".format(i, current_energy))
                # Eğer yeni çözüm, şu ana kadar en iyi çözümden daha iyiyse, en iyi çözüm güncellenir
                if current_energy < best_energy:
                    best_solution = current_solution
                    file.write("{} best solution = {}\n".format(i, current_solution))
                    best_energy = current_energy
                    file.write("{} best energy = {}\n".format(i, current_energy))
            # Sıcaklık, soğuma oranına göre azaltılır
            temperature *= cooling_rate
            file.write("{} temperature reduced: {}\n".format(i, temperature))
            file.write("\n")
        # En iyi çözüm ve enerjiyi döndürür
    return best_solution, best_energy

# Parametreler
initial_temperature = 100
cooling_rate = 0.99

# Simulated Annealing'i çalıştır
best_solution, best_energy = simulated_annealing(initial_solution, energy, neighbor, acceptance_probability, initial_temperature, cooling_rate)

with open(output_file, "a") as file:
    file.write("initial parameters: {}\n")
    file.write("initial_temperature : {}\n".format(initial_temperature))
    file.write("cooling_rate: {}\n".format(cooling_rate))
    
# Sonuçları ekrana yazdır
with open(output_file, "a") as file:
    file.write("En iyi çözüm: {}\n".format(best_solution))
    file.write("En iyi enerji: {}\n".format(best_energy))
    file.write("\n\n\n---------------------------------------------------------------------------------\n\n\n")
    
