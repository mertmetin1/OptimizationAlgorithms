import math
import random

# Çıktı dosyası
output_file = "SA_TSP_solution_Mert.txt"
with open(output_file, "a") as file:



    def energy(solution):
        sum=0
        for i in range(len(initial_solution)-1):
            sum+=roadmatrix[solution[i]-1][solution[i+1]-1]
  
        
        return sum

    def swap(solution,i1,i2):
        a =solution[i1]
        solution[i1]=solution[i2]
        solution[i2]=a

        return solution

    def move(solution):
        r1=random.randint(0,len(solution)-1)
        r2=random.randint(0,len(solution)-1)
        solution =swap(solution,r1,r2)
        
        return solution



    cities = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    file.write("Cities: {}\n".format(cities))
    roadmatrix = [
    #city 1   2   3   4   5   6   7   8   9    
        [0, 10, 15, 20, 25, 37, 43, 51, 62],  # 1
        [10, 0, 35, 25, 30, 23, 12, 19, 26],  # 2
        [15, 35, 0, 30, 20, 30, 26, 56, 47],  # 3
        [20, 25, 30, 0, 18, 42, 33, 60, 65],  # 4
        [25, 30, 20, 18, 0, 49, 40, 70, 78],  # 5
        [37, 23, 30, 42, 49, 0, 67, 77, 89],  # 6
        [43, 12, 26, 33, 40, 67, 0, 93, 103], # 7
        [51, 19, 56, 60, 70, 77, 93, 0, 123], # 8
        [62, 26, 47, 65, 78, 89, 103, 123, 0] # 9
    ]
    a="""
    
    #city 1   2   3   4   5   6   7   8   9    
        [0, 10, 15, 20, 25, 37, 43, 51, 62],  # 1
        [10, 0, 35, 25, 30, 23, 12, 19, 26],  # 2
        [15, 35, 0, 30, 20, 30, 26, 56, 47],  # 3
        [20, 25, 30, 0, 18, 42, 33, 60, 65],  # 4
        [25, 30, 20, 18, 0, 49, 40, 70, 78],  # 5
        [37, 23, 30, 42, 49, 0, 67, 77, 89],  # 6
        [43, 12, 26, 33, 40, 67, 0, 93, 103], # 7
        [51, 19, 56, 60, 70, 77, 93, 0, 123], # 8
        [62, 26, 47, 65, 78, 89, 103, 123, 0] # 9
    ]
    
    """
    file.write("RoadMatrix:\n {}\n".format(a))
    
    temperature=100
    coolrate=0.93
    initial_solution = [4, 2, 8, 1, 3, 5, 9, 6, 7]
    
    file.write("initial selected solution :{}\n".format(initial_solution))
    file.write("initial energy {}\n".format(energy(initial_solution)))
    file.write("temperature : {}\n".format(temperature))
    file.write("cooling Rate : {}\n".format(coolrate))

    best_solution=initial_solution
    best_energy=energy(initial_solution)
    
    last_solution=initial_solution
    last_energy=energy(initial_solution)
    
    i=0
    while(temperature>0.1):
        i+=1
        current_solution=move(last_solution)
        file.write(str(i)+" Random Walk(swapped) Current Solution  : {} to \n".format(current_solution))
        current_energy=energy(last_solution)
        file.write(str(i)+" current energy : {}\n".format(current_energy))      
        
        delta = energy(current_solution) - energy(last_solution)
        probability = math.exp(-delta / temperature)
        print(math.exp(-delta/temperature))
        file.write("{} Probability: {}\n".format(i, probability))
        
        if delta < 0 or random.random() < probability:
            
            last_solution=current_solution
            last_energy=current_energy

            
            if last_energy<best_energy:
                best_solution=last_solution
                best_energy=last_energy
                file.write(str(i)+" last > best ")
                file.write(str(i)+"  best solution : {}\n".format(best_solution))
                file.write(str(i)+" best energy: {}\n".format(best_energy))
        
        temperature*=coolrate
        file.write("\n"+str(i)+"------------------------------------------------------------------------------------------------------\n")





