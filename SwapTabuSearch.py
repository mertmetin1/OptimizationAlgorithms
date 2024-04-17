import random
import time
def distance(solution, roadmatrix):
    sum = 0
    for i in range(len(solution) - 1):
        sum += roadmatrix[solution[i] - 1][solution[i + 1] - 1]
    return sum

def move(solution):
    i1, i2 = random.sample(range(len(solution)), 2)
    solution[i1], solution[i2] = solution[i2], solution[i1]
    return solution, (i1, i2)


def SwapTabuSearch(initial_solution,tabu_len, max_iteration, roadmatrix):
    tabu_set = set()
    
    best_solution = initial_solution.copy()
    best_distance = distance(best_solution, roadmatrix)
    
    current_solution = initial_solution.copy()
    current_distance=distance(current_solution, roadmatrix)
    for i in range(max_iteration):
        
        
        neighbours=[]
        for k in range(5):
            
            new_solution,swap=move(current_solution)
            neighbours.append((new_solution,swap,distance(new_solution, roadmatrix)))
        neighbours=sorted(neighbours, key=lambda x: x[2])

        
        for new_solution,swap,new_distance in neighbours:
            
            if len(tabu_set) == tabu_len:
                tabu_set.pop()
                            
            if swap not in tabu_set:
                if new_distance < current_distance :
                    current_solution = new_solution
                    if distance(new_solution, roadmatrix) < best_distance:
                        best_solution = new_solution
                        best_distance = new_distance
                        
                        #print(" CurrentBest :",best_distance,best_solution," ",i,)
                        
                        tabu_set.add(swap)
                        break
                tabu_set.add(swap)

    return best_solution, best_distance

roadmatrix = [
    [0,   10,  15,  20,  25,  37,  43,  51,  62,  70,  80,  90,  100, 110, 120, 130, 140, 150, 160, 170],
    [10,  0,   35,  25,  30,  23,  12,  19,  26,  35,  45,  55,  65,  75,  85,  95,  105, 115, 125, 135],
    [15,  35,  0,   30,  20,  30,  26,  56,  47,  52,  62,  72,  82,  92,  102, 112, 122, 132, 142, 152],
    [20,  25,  30,  0,   18,  42,  33,  60,  65,  38,  48,  58,  68,  78,  88,  98,  108, 118, 128, 138],
    [25,  30,  20,  18,  0,   49,  40,  70,  78,  57,  67,  77,  87,  97,  107, 117, 127, 137, 147, 157],
    [37,  23,  30,  42,  49,  0,   67,  77,  89,  88,  98,  108, 118, 128, 138, 148, 158, 168, 178, 188],
    [43,  12,  26,  33,  40,  67,  0,   93,  103, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],
    [51,  19,  56,  60,  70,  77,  93,  0,   123, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220],
    [62,  26,  47,  65,  78,  89,  103, 123, 0,   154, 164, 174, 184, 194, 204, 214, 224, 234, 244, 254],
    [70,  35,  52,  38,  57,  88,  100, 120, 154, 0,   180, 190, 200, 210, 220, 230, 240, 250, 260, 270],
    [80,  45,  62,  48,  67,  98,  110, 130, 164, 180, 0,   220, 230, 240, 250, 260, 270, 280, 290, 300],
    [90,  55,  72,  58,  77,  108, 120, 140, 174, 190, 220, 0,   260, 270, 280, 290, 300, 310, 320, 330],
    [100, 65,  82,  68,  87,  118, 130, 150, 184, 200, 230, 260, 0,   290, 300, 310, 320, 330, 340, 350],
    [110, 75,  92,  78,  97,  128, 140, 160, 194, 210, 240, 270, 290, 0,   320, 330, 340, 350, 360, 370],
    [120, 85,  102, 88,  107, 138, 150, 170, 204, 220, 250, 280, 300, 320, 0,   350, 360, 370, 380, 390],
    [130, 95,  112, 98,  117, 148, 160, 180, 214, 230, 260, 290, 310, 330, 350, 0,   370, 380, 390, 400],
    [140, 105, 122, 108, 127, 158, 170, 190, 224, 240, 270, 300, 320, 340, 360, 370, 0,   390, 400, 410],
    [150, 115, 132, 118, 137, 168, 180, 200, 234, 250, 280, 310, 330, 350, 370, 380, 390, 0,   410, 420],
    [160, 125, 142, 128, 147, 178, 190, 210, 244, 260, 290, 320, 340, 360, 380, 390, 400, 410, 0,   430],
    [170, 135, 152, 138, 157, 188, 200, 220, 254, 270, 300, 330, 350, 370, 390, 400, 410, 420, 430, 0  ]
]

"""
En iyi mesafe: 2508

Best Solution: 2528 [1, 18, 5, 11, 13, 17, 19, 3, 7, 6, 14, 8, 10, 2, 16, 9, 20, 15, 12, 4]  tabu set:  100 iterasyon:  100000

initial Solution : 3403 [11, 18, 2, 5, 4, 1, 7, 14, 19, 13, 17, 12, 10, 8, 16, 15, 3, 20, 9, 6]
Best Solution: 2586 [14, 12, 3, 9, 5, 6, 1, 18, 20, 7, 10, 4, 11, 17, 15, 19, 16, 13, 8, 2]  tabu set:  100 iterasyon:  100000

initial Solution : 2740 [12, 8, 15, 5, 14, 9, 6, 18, 4, 7, 11, 13, 16, 2, 17, 3, 20, 1, 10, 19]
Best Solution: 2516 [3, 6, 7, 14, 20, 17, 8, 5, 4, 10, 18, 16, 2, 13, 11, 1, 12, 15, 19, 9]  tabu set:  100 iterasyon:  100000




"""

lifetimescores=[]
tabusize=30
max_iter=9909
initial_solution = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]
for i in range(100):
    start_time = time.time()

    best_solution, best_distance = SwapTabuSearch(initial_solution, tabusize, max_iter, roadmatrix)
    #print("initial Solution :",distance(initial_solution,roadmatrix),initial_solution)
    #print("Best Solution:", best_distance, best_solution," tabu set: ",tabusize,"iterasyon: ",max_iter)
    end_time = time.time()
    execution_time = end_time - start_time
    
    #print("Kodun çalışma süresi:", execution_time, "saniye")
    print(distance(initial_solution,roadmatrix),best_distance,tabusize,max_iter,execution_time)
    lifetimescores.append((initial_solution,distance(initial_solution,roadmatrix),best_solution,best_distance,tabusize,max_iter,execution_time))

