import random

def objective_function(x):
    """Minimize edilmek istenen fonksiyon."""
    return (x - 2) ** 2  # Örnek bir fonksiyon, bu örnekte (x - 2) ^ 2

def generate_neighbour(current, step_size):
    """Mevcut konumdan rastgele bir adım uzaklıkta bir komşu üretir."""
    return current + random.randint(-step_size, step_size)

def select_neighbour(neighbours):
    """Üretilen komşu çözümler arasından birini seçer."""
    return random.choice(neighbours)

def tabu_search(initial_solution, max_iter, step_size, tabu_list_size):
    """Tabu arama algoritması."""
    current_solution = initial_solution
    best_solution = current_solution
    tabu_list = []

    for _ in range(max_iter):
        print("iterasyon : ",_)
        print("current solution : ",current_solution)
        neighbours = [generate_neighbour(current_solution, step_size) for _ in range(5)] # Komşu çözümleri üret
        
        results = [(candidate_solution, objective_function(candidate_solution)) for candidate_solution in neighbours]
        neighbours = sorted(results, key=lambda x: x[1]) # Sonuçları büyükten küçüğe sıralayalım
        print("neighbours of current solution  : ",neighbours)
        
        
        for candidate_solution,candidate_fitness in neighbours :

            
            if candidate_solution not in tabu_list:
                print("         for candicate : " ,candidate_solution)
                print("         tabu : " ,candidate_solution in tabu_list)
                print("         better fitness : ",objective_function(candidate_solution) < objective_function(current_solution))
                if objective_function(candidate_solution) < objective_function(current_solution):
               
                    current_solution = candidate_solution
                    print("         current solution ile dğeiştir")  

                    if objective_function(candidate_solution) < objective_function(best_solution):
                        best_solution = candidate_solution
                        print("all time best : ",candidate_solution)
                        print()
                        break
            else:
                print("         for candicate : " ,candidate_solution)
                print("         tabu : " ,candidate_solution in tabu_list)
                print("         better fitness : ",objective_function(candidate_solution) < objective_function(current_solution))
                
           
            # Tabu listesini güncelle
            tabu_list.append(candidate_solution)
            print("         tabu listesibe eklendi: ",candidate_solution)
            
            
            if len(tabu_list) > tabu_list_size:
                print("         tabu listesinden çıkartıldı : " ,tabu_list[0])
                tabu_list.pop(0)
            
            
            print()
   
   
    return best_solution

# Başlangıç noktası
initial_solution = 1010000
# Maksimum iterasyon sayısı
max_iter = 10000
# Adım büyüklüğü
step_size = 100
# Tabu listesi boyutu
tabu_list_size = 500

# Tabu arama algoritmasını çalıştır
best_solution = tabu_search(initial_solution, max_iter, step_size, tabu_list_size)


print("initial solution :" ,initial_solution)
print("initial çözümün değeri:", objective_function(initial_solution))
print("En iyi çözüm:", best_solution)
print("En iyi çözümün değeri:", objective_function(best_solution))
