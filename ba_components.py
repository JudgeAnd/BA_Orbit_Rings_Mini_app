class BAPlanet:
    def __init__(self, R, theta, omega, size, color):
        self.R = R
        self.theta = theta
        self.omega = omega
        self.size = size
        self.color = color

class BAAppState:
    def __init__(self, planets, center, info_turtle):
        self.planets = planets
        self.center = center
        self.info_turtle = info_turtle
        self.speed = 1.0
        self.running = True