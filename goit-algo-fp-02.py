import turtle

def draw_pifagoras_tree(branch_len, level):
    if level == 0:
        return
    # Намалювати основну гілку
    turtle.forward(branch_len)
    turtle.left(45)
    draw_pifagoras_tree(0.6 * branch_len, level - 1)
    # Повернутися і намалювати праву гілку
    turtle.right(90)
    draw_pifagoras_tree(0.6 * branch_len, level - 1)
    # Повернутися і намалювати ліву гілку
    turtle.left(45)
    turtle.backward(branch_len)

def main():
    level = int(input("Введіть рівень рекурсії: "))
    
    # Налаштування вікна для візуалізації
    turtle.speed(0)  # Найшвидша швидкість
    turtle.bgcolor("white")
    turtle.color("green")
    turtle.left(90)  # Початковий кут

    # Початок малювання фрактала
    draw_pifagoras_tree(100, level)

    # Завершення роботи
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()