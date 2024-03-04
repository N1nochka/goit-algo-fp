import random
import matplotlib.pyplot as plt

def roll_dice():
    return random.randint(1, 6)

def simulate_dice_rolls(num_trials):
    sums_count = {i: 0 for i in range(2, 13)}
    for _ in range(num_trials):
        dice1 = roll_dice()
        dice2 = roll_dice()
        total = dice1 + dice2
        sums_count[total] += 1
    return sums_count

def plot_probabilities(probabilities, num_trials):
    plt.bar(probabilities.keys(), probabilities.values(), label=f'num_trials={num_trials}')
    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Імовірність')
    plt.title('Імовірності сум чисел на двох кубиках (Метод Монте-Карло)')
    plt.xticks(range(2, 13))
    plt.legend()
    plt.show()

def main():
    num_trials_values = [100, 1000, 10000]  # Різні значення num_trials
    for num_trials in num_trials_values:
        sums_count = simulate_dice_rolls(num_trials)
        probabilities = {total: count / num_trials * 100 for total, count in sums_count.items()}
        print(f"=== Результати для num_trials = {num_trials} ===")
        print("Сума\tІмовірність (Монте-Карло)\tІмовірність (Аналітично)")
        for total, probability in probabilities.items():
            analytical_probability = 0
            if total <= 7:
                analytical_probability = (total - 1) / 36 * 100
            else:
                analytical_probability = (13 - total) / 36 * 100
            print(f"{total}\t{probability:.2f}%\t\t\t{analytical_probability:.2f}%")
        print()
        
        plot_probabilities(probabilities, num_trials)

if __name__ == "__main__":
    main()
