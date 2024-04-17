import math
import random

output_file = "SA_TSP_solution_Mert.txt"
with open(output_file, "a") as file:
    def energy(solution, road_matrix):
        total_dist = 0
        for i in range(len(solution) - 1):
            total_dist += road_matrix[solution[i] - 1][solution[i + 1] - 1]
        total_dist += road_matrix[solution[-1] - 1][solution[0] - 1]  # back to start
        return total_dist

    def swap(solution, i1, i2):
        solution[i1], solution[i2] = solution[i2], solution[i1]
        return solution

    def move(solution):
        r1 = random.randint(0, len(solution) - 1)
        r2 = random.randint(0, len(solution) - 1)
        return swap(solution[:], r1, r2)

    cities = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    file.write("Cities: {}\n".format(cities))

    roadmatrix = [
        [0, 10, 15, 20, 25, 37, 43, 51, 62],  # 1
        [10, 0, 35, 25, 30, 23, 12, 19, 26],  # 2
        [15, 35, 0, 30, 20, 30, 26, 56, 47],  # 3
        [20, 25, 30, 0, 18, 42, 33, 60, 65],  # 4
        [25, 30, 20, 18, 0, 49, 40, 70, 78],  # 5
        [37, 23, 30, 42, 49, 0, 67, 77, 89],  # 6
        [43, 12, 26, 33, 40, 67, 0, 93, 103],  # 7
        [51, 19, 56, 60, 70, 77, 93, 0, 123],  # 8
        [62, 26, 47, 65, 78, 89, 103, 123, 0]  # 9
    ]
    file.write("RoadMatrix:\n {}\n".format(roadmatrix))

    temperature = 100
    coolrate = 0.93
    initial_solution = [4, 2, 8, 1, 3, 5, 9, 6, 7]

    file.write("Initial selected solution: {}\n".format(initial_solution))
    file.write("Initial energy: {}\n".format(energy(initial_solution, roadmatrix)))
    file.write("Temperature: {}\n".format(temperature))
    file.write("Cooling Rate: {}\n".format(coolrate))

    best_solution = initial_solution
    best_energy = energy(initial_solution, roadmatrix)

    last_solution = initial_solution
    last_energy = energy(initial_solution, roadmatrix)

    i = 0
    while temperature > 0.1:
        i += 1
        current_solution = move(last_solution)
        file.write("{} Random Walk (swapped) Current Solution: {}\n".format(i, current_solution))
        current_energy = energy(current_solution, roadmatrix)
        file.write("{} Current energy: {}\n".format(i, current_energy))

        delta = energy(current_solution, roadmatrix) - energy(last_solution, roadmatrix)
        probability = math.exp(-delta / temperature)
        file.write("{} Probability: {}\n".format(i, probability))

        if delta < 0 or random.random() < probability:
            last_solution = current_solution
            last_energy = current_energy

            if last_energy < best_energy:
                best_solution = last_solution
                best_energy = last_energy
                file.write("{} Last > Best\n".format(i))
                file.write("{} Best solution: {}\n".format(i, best_solution))
                file.write("{} Best energy: {}\n".format(i, best_energy))

        temperature *= coolrate
        file.write("\n{} ----------------------------------------------------------------\n".format(i))
