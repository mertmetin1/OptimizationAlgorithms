import math
import random

matrix=[
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
temp=100


def swap(solution,i1,i2):
   
    t=solution[i2]
    solution[i2]=solution[i1]
    solution[i1]=t
    return solution
    
def move(solution):
    r1=random.randint(0,len(solution)-1)
    r2=random.randint(0,len(solution)-1)
    swap(solution,r1,r2)
    return solution

def distance(solution):
    sum=0
    for i in range(len(solution)-1):
        sum+=matrix[solution[i]-1][solution[i+1]-1]
    return sum

solution=[4, 2, 8, 1, 3, 5, 9, 6, 7]


def SA(solution):
    temp=1000
    cool=0.99
    last_solution=solution
    best_solution=solution
    best_distance=distance(last_solution)
    while(temp>0.1):
        current_solution=move(last_solution) 
        current_distance=distance(last_solution)
        temp*=cool
        for i in range(1000):
            delta = distance(current_solution) - distance(last_solution)
            probability = math.exp(-delta / temp)
            if delta < 0 or random.random() < probability:
                last_solution=current_solution
                if best_distance >current_distance:
                    best_distance=current_distance
                    best_solution=current_solution
                    print("best distance : ",best_distance)
                    print("best solution :",best_solution)      
    
SA(solution)      
    
        
