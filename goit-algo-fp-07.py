import random
import matplotlib.pyplot as plt

def roll_dice():
    return random.randint(1, 6)

def simulate_dice_rolls(num_trials):
    sums_count = {i: 0 for i in range(2, 13)}  # Ініціалізуємо словник для підрахунку кількості кожної суми
    for _ in range(num_trials):
        dice1 = roll_dice()
        dice2 = roll_dice()
        total = dice1 + dice2
        sums_count[total] += 1
    return sums_count

def plot_probabilities(probabilities):
    plt.bar(probabilities.keys(), probabilities.values())
    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Імовірність')
    plt.title('Імовірності сум чисел на двох кубиках (Метод Монте-Карло)')
    plt.xticks(range(2, 13))
    plt.show()

def main():
    num_trials = 1000000
    sums_count = simulate_dice_rolls(num_trials)
    probabilities = {total: count / num_trials * 100 for total, count in sums_count.items()}
    plot_probabilities(probabilities)

    print("Сума\tІмовірність")
    for total, probability in probabilities.items():
        print(f"{total}\t{probability:.2f}%")

if __name__ == "__main__":
    main()
