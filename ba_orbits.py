from math import sin, cos, pi

def BA_wrap_angle(theta):
    return theta % (2*pi)

def BA_polar_to_cart(cx, cy, r, theta):
    return cx + r*cos(theta), cy + r*sin(theta)

def BA_step(planets, speed_scale, dt):
    for p in planets:
        p.theta = BA_wrap_angle(p.theta + p.omega*dt*speed_scale)