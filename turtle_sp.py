import turtle

# Создаем экран для рисования
screen = turtle.Screen()
screen.bgcolor("white")  # Задаем белый цвет фона экрана
screen.setup(width=800, height=600)

# Создаем черепашку
t = turtle.Turtle()
t.shape("turtle")  # Форма черепашки (можно использовать "turtle", "square", "triangle", "circle", "classic")

# Рисуем квадрат с изменением размера и цвета черепашки
t.color("blue")  # Задаем цвет черепашки
for size in range(1, 6):
    t.pensize(size)  # Устанавливаем толщину пера
    for _ in range(4):
        t.forward(100)  # Двигаем черепашку вперед на 100 пикселей
        t.right(90)     # Поворачиваем черепашку на 90 градусов вправо
    t.color("red")  # Меняем цвет перед рисованием следующего квадрата

# Рисуем треугольник
t.penup()
t.goto(-150, 0)
t.pendown()
t.color("green")
for _ in range(3):
    t.forward(100)
    t.left(120)


t.shape("triangle")  # Меняем форму черепашки на треугольник
t.color("purple")    # Меняем цвет черепашки
t.penup()
t.goto(-50, -50)     # Перемещаем черепашку в начальную позицию анимации
t.pendown()

t.speed(10) # 1-slowest, 3-slow, 6-normal, 10-fast, 0-fastest;
for _ in range(90):
    t.forward(8)
    t.left(4)

# Завершаем работу
turtle.done()
