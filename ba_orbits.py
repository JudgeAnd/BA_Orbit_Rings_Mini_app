from math import sin, cos, pi

def BA_step(planets, speed_scale, dt):
    for p in planets:
        p.theta += p.omega*dt*speed_scale
        if p.theta > 2*pi:
            p.theta -= 2*pi
        if p.theta < 0:
            p.theta += 2*pi