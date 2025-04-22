import turtle

screen = turtle.Screen()
screen.title("Космические гаджеты")
screen.bgcolor("white")
screen.setup(width=1400, height=600)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

square_size = 250
gap = 40
start_x = -600
y_pos = 100


def draw_square(x, y, size, color="black"):
    t.penup()
    t.goto(x - size / 2, y - size / 2)
    t.pendown()
    t.color(color)
    for _ in range(4):
        t.forward(size)
        t.left(90)


def draw_circle(x, y, radius, color):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def draw_rect(x, y, width, height, color):
    t.penup()
    t.goto(x - width / 2, y - height / 2)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()


def draw_light_sword(x, y, color):
    handle_width = 40
    handle_height = 120
    draw_rect(x, y + 20, handle_width, handle_height, "#888888")

    draw_circle(x, y + 40, 8, "black")
    draw_circle(x, y, 8, "black")

    t.penup()
    t.goto(x, y - handle_height / 2 + 20)
    t.pendown()
    t.color(color)
    t.pensize(12)
    t.goto(x, y - handle_height / 2 - 80)
    t.pensize(1)


def draw_phaser(x, y):
    body_width = 120
    body_height = 40
    draw_rect(x, y, body_width, body_height, "#1155AA")

    barrel_width = 50
    barrel_height = 20
    draw_rect(x + body_width / 2 - barrel_width / 2, y, barrel_width, barrel_height, "#44AAFF")

    draw_circle(x - 30, y, 10, "red")
    draw_circle(x - 10, y, 10, "yellow")
    draw_circle(x + 10, y, 10, "green")


def draw_gravity_gun(x, y):
    body_width = 140
    body_height = 50
    draw_rect(x, y, body_width, body_height, "#666666")

    barrel_width = 60
    barrel_height = 30
    draw_rect(x + body_width / 2 - barrel_width / 2, y, barrel_width, barrel_height, "#AAAAAA")

    draw_circle(x - 20, y, 18, "#2222FF")
    draw_circle(x + 20, y, 18, "#2222FF")


def draw_plasma_cutter(x, y):
    body_width = 100
    body_height = 30
    draw_rect(x, y, body_width, body_height, "#C0C0C0")

    barrel_width = 40
    barrel_height = 15
    draw_rect(x + body_width / 2 - barrel_width / 2, y, barrel_width, barrel_height, "#FFD700")

    t.penup()
    t.goto(x + body_width / 2, y)
    t.pendown()
    t.color("red")
    t.pensize(5)
    t.goto(x + body_width / 2 + 40, y)
    t.pensize(1)


def draw_sonic_screwdriver(x, y):
    body_width = 30
    body_height = 150
    draw_rect(x, y - 20, body_width, body_height, "#0066CC")

    draw_rect(x, y + 30, body_width + 10, 10, "#88CCFF")
    draw_rect(x, y, body_width + 10, 10, "#88CCFF")
    draw_rect(x, y - 30, body_width + 10, 10, "#88CCFF")

    tip_width = 40
    tip_height = 20
    draw_rect(x, y - body_height / 2 + 10, tip_width, tip_height, "#FFCC00")


positions = [start_x + i * (square_size + gap) for i in range(5)]

for i, x in enumerate(positions):
    draw_square(x, y_pos, square_size)

    if i == 0:
        draw_light_sword(x, y_pos, "red")
    elif i == 1:
        draw_phaser(x, y_pos)
    elif i == 2:
        draw_gravity_gun(x, y_pos)
    elif i == 3:
        draw_plasma_cutter(x, y_pos)
    elif i == 4:
        draw_sonic_screwdriver(x, y_pos)

labels = ["Световой меч", "Фазер", "Гравипушка", "Плазморез", "Звуковая отвертка"]
for i, x in enumerate(positions):
    t.penup()
    t.goto(x, y_pos - square_size / 2 - 30)
    t.color("black")
    t.write(labels[i], align="center", font=("Arial", 14, "bold"))

turtle.done()