import turtle
import random
from math import radians
from ba_orbits import BA_step, BA_polar_to_cart
from ba_components import BAPlanet, BAAppState

root = turtle.Screen()
root.title("BA Orbit Rings Mini")
root.bgcolor("white")
turtle.colormode(255)
turtle.tracer(0, 0)

orb_t = turtle.Turtle(visible=False)
planet_t = turtle.Turtle(visible=False)
info_t = turtle.Turtle(visible=False)
for t in (orb_t, planet_t, info_t):
    t.hideturtle()
    t.speed(0)
planet_t.pensize(4)

app = BAAppState([], (0, 0), info_t)

def BA_redraw():
    orb_t.clear()
    planet_t.clear()
    cx, cy = app.center
    orb_t.pencolor("#999999")
    for p in app.planets:
        orb_t.penup()
        orb_t.goto(cx, cy - p.R)
        orb_t.pendown()
        orb_t.circle(p.R)
    for p in app.planets:
        x, y = BA_polar_to_cart(cx, cy, p.R, p.theta)
        planet_t.penup()
        planet_t.goto(x, y - p.size)
        planet_t.pendown()
        planet_t.pencolor("black")
        planet_t.fillcolor(p.color)
        planet_t.begin_fill()
        planet_t.circle(p.size)
        planet_t.end_fill()
    info_t.clear()
    info_t.penup()
    info_t.goto(-root.window_width()//2 + 16, root.window_height()//2 - 36)
    info_t.write(f"planets={len(app.planets)}  speed×{app.speed:.2f}", font=("Arial", 12, "normal"))
    turtle.update()

def BA_anim():
    if app.running:
        BA_step(app.planets, app.speed, 0.03)
    BA_redraw()
    root.ontimer(BA_anim, 30)

def BA_add_planet(x=None, y=None):
    if x is not None and y is not None:
        cx, cy = app.center
        dx, dy = x - cx, y - cy
        r = max(30, int((dx*dx + dy*dy) ** 0.5))
    else:
        r = random.randrange(50, 260)
    size = random.randrange(6, 12)
    omega = random.choice([-1, 1]) * random.uniform(0.2, 1.0)
    theta = radians(random.uniform(0, 360))
    color = (random.randrange(0,256), random.randrange(0,256), random.randrange(0,256))
    app.planets.append(BAPlanet(r, theta, omega, size, color))

def BA_remove():
    if app.planets:
        app.planets.pop()

def BA_speed_up():
    app.speed = min(5.0, app.speed + 0.2)

def BA_speed_down():
    app.speed = max(0.2, app.speed - 0.2)

def BA_toggle_run():
    app.running = not app.running

def BA_move_center(x, y):
    app.center = (int(x), int(y))

def BA_quit():
    turtle.bye()

for _ in range(4):
    BA_add_planet()

BA_redraw()
BA_anim()

root.listen()
root.onkey(BA_add_planet, "n")
root.onkey(BA_remove, "Delete")
root.onkey(BA_speed_up, "x")
root.onkey(BA_speed_down, "z")
root.onkey(BA_toggle_run, "space")
root.onkey(BA_quit, "Escape")
root.onscreenclick(BA_move_center)

turtle.mainloop()