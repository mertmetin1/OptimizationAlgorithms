# Optimization Algorithms

This repository contains implementations of various optimization algorithms commonly used in solving different types of problems. Each algorithm is described below along with its key components and operation.
Metaheuristics are a flexible and powerful class of algorithms used to solve various optimization problems. These approaches are designed to find effective solutions in complex and often uncertain problem domains. Metaheuristics typically employ a guided search strategy to explore solutions in a search space and generally do not guarantee optimal solutions but aim to produce acceptable solutions.

## Backtracking Algorithm (BT)

The fundamental algorithm used for solving Sudoku puzzles is backtracking. This algorithm assigns a number to an empty cell and checks if it satisfies the rules. If it does, the process continues; otherwise, it backtracks and tries a different number. Before each assignment, the algorithm checks whether the assigned number already exists in the same row, column, or 3x3 subgrid. This step ensures adherence to the basic rules of Sudoku. At each step of solving the Sudoku puzzle, the algorithm searches for an empty cell in the unsolved puzzle. If no empty cells are found, the puzzle is considered solved. Sudoku solving is based on a recursive structure built upon the backtracking algorithm.

![Sudoku Solver](https://github.com/mertmetin1/OptimizationAlgorithms/assets/98667673/3f3ff38a-04aa-47bb-b0ab-16fe9ef20ef5)

## Particle Swarm Optimization Algorithm (PSO)

Particle Swarm Optimization (PSO) is a population-based stochastic optimization technique. In this algorithm, random positions and velocities are assigned to particles within the search space. The objective function is evaluated at each particle's position to determine its fitness. The new velocity of each particle is calculated based on its current velocity, personal best position, and the global best position found by any particle. The particle's position is updated using the new velocity, moving it towards promising regions in the search space. PSO iteratively refines solutions until a satisfactory solution is found.

![PSO Algorithm](https://github.com/mertmetin1/OptimizationAlgorithms/assets/98667673/df73e643-e46e-4ee1-babc-78b0a14d0721)

## Genetic Algorithm (GA)

Genetic Algorithm (GA) is a heuristic search algorithm inspired by the process of natural selection. In this implementation, GA is applied to solve the knapsack problem. Random parents representing potential solutions to the knapsack problem are generated initially. The fitness function evaluates the total value of items in the knapsack, considering the items selected by each parent. Parents are selected based on their fitness, favoring those with higher total values. Crossover and mutation operations are applied to produce offspring with potentially better solutions. The fittest individuals, including parents and offspring, are chosen to survive and form the next generation.

![Genetic Algorithm](https://github.com/mertmetin1/OptimizationAlgorithms/assets/98667673/e78b6b99-d249-48aa-b8b3-05c37b0d1977)

## Simulated Annealing Optimization Algorithm (SA)

Simulated Annealing is a probabilistic optimization technique inspired by the annealing process in metallurgy. Random initial solutions are generated within the search space. The energy function evaluates the quality of a solution. Neighborhood exploration involves perturbing the current solution within a certain range. The probability of accepting a new solution is determined based on the energy difference between the current and new solutions, as well as the current temperature. The temperature is gradually decreased over iterations according to a cooling rate. Simulated Annealing effectively explores the search space and can escape local optima.

![Simulated Annealing](https://github.com/mertmetin1/OptimizationAlgorithms/assets/98667673/ebae155b-d343-41e1-992f-157118d2b5f1)

## Tabu Search Optimization Algorithm (TS)

Tabu Search is a metaheuristic optimization technique used for solving combinatorial optimization problems. An initial solution is randomly generated, representing a possible solution. The algorithm iterates through a specified number of iterations, exploring neighboring solutions by swapping cities in the current solution. A tabu list is maintained to avoid revisiting previously explored solutions. The objective function evaluates the quality of each solution. The best solution found so far is updated throughout the iterations. Tabu Search effectively explores the solution space and can find near-optimal solutions.

![Tabu Search](https://github.com/mertmetin1/OptimizationAlgorithms/assets/98667673/0314ed3f-b31c-4d9b-ac3d-63ca0e7782ea)

## Brute Force Optimization Algorithm (BF)

Brute Force is a straightforward approach to optimization where all possible solutions are explored. Each combination of items is encoded into a binary string, representing whether the item is selected or not. The algorithm iterates through a predefined number of iterations, randomly sampling combinations of items. For each combination, the algorithm calculates the total weight and profit, checking if the weight constraint is satisfied. The best solution found is updated throughout the iterations. Brute Force guarantees finding the optimal solution but can be computationally expensive for large problem instances.

![Brute Force](https://github.com/mertmetin1/OptimizationAlgorithms/assets/98667673/d69bcd3b-2fdb-4005-8fd7-3bacf94907a3)

