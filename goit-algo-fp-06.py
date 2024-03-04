def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    selected_items = []
    total_cost = 0
    total_calories = 0

    for item, info in sorted_items:
        if total_cost + info["cost"] <= budget:
            selected_items.append(item)
            total_cost += info["cost"]
            total_calories += info["calories"]

    return selected_items, total_cost, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        item_name = list(items.keys())[i - 1]
        item_cost = items[item_name]["cost"]
        item_calories = items[item_name]["calories"]
        for j in range(1, budget + 1):
            if item_cost > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - item_cost] + item_calories)
    
    optimal_items = []
    i, j = n, budget
    while i > 0 and j > 0:
        item_name = list(items.keys())[i - 1]
        item_cost = items[item_name]["cost"]
        item_calories = items[item_name]["calories"]
        if dp[i][j] != dp[i - 1][j]:
            optimal_items.append(item_name)
            j -= item_cost
        i -= 1
    
    optimal_cost = sum(items[item]["cost"] for item in optimal_items)
    optimal_calories = sum(items[item]["calories"] for item in optimal_items)
    
    return optimal_items, optimal_cost, optimal_calories

# Приклад використання
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100
greedy_items, greedy_cost, greedy_calories = greedy_algorithm(items, budget)
dynamic_items, dynamic_cost, dynamic_calories = dynamic_programming(items, budget)

print("Greedy Algorithm:")
print("Selected items:", greedy_items)
print("Total cost:", greedy_cost)
print("Total calories:", greedy_calories)

print("\nDynamic Programming:")
print("Selected items:", dynamic_items)
print("Total cost:", dynamic_cost)
print("Total calories:", dynamic_calories)
