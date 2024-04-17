import random


def encode_to_binary(combination, initial_parent):
    binary = ""
    for parent in initial_parent:
        if parent in combination:
            binary += "1"
        else:
            binary += "0"
    return binary


def knapsack_brute_force(weights, profits, capacity):
    n = len(weights)
    max_profit = 0
    best_combination = []

    # Tüm olası kombinasyonları deneyerek en yüksek karı bul
    for i in range(100):
        ran=random.randint(0,2**10)
        current_weight = 0
        current_profit = 0
        combination = []

        for j in range(n):
        
            if (ran >> j) & 1: 
                current_weight += weights[j]
                current_profit += profits[j]
                combination.append(j)

        if current_weight <= capacity and current_profit > max_profit:
            max_profit = current_profit
            best_combination = combination



         

        
    
    return max_profit, best_combination

# Örnek veri
weights = [2, 3, 4, 5]
profits = [3, 4, 5, 6]
capacity = 5

# Knapsack problemi çözümü (Kaba kuvvet yöntemi)
max_profit, best_combination = knapsack_brute_force(weights, profits, capacity)

print("Maksimum Kar:", max_profit)
print("En iyi Kombinasyonun İndeksleri:", best_combination)
