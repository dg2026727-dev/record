Web VPython 3.2

scene = canvas(title="VPython 디테일 비행기 조종하기", width=1000, height=700, center=vec(0, 0, -2))
scene.background = vec(0.2, 0.2, 0.2)

body = cylinder(pos=vec(0, 0, 0), axis=vec(0, 0, -4), radius=0.4, color=vec(0.8, 0.8, 0.8))
nose = cone(pos=vec(0, 0, 0), axis=vec(0, 0, 0.8), radius=0.4, color=color.red)
win = ellipsoid(pos=vec(0, 0.3, -0.8), length=1.2, height=0.4, width=0.4, color=color.cyan, opacity=0.6)


wing_left = box(pos=vec(-2, -0.1, -1.8), size=vec(4, 0.05, 1.2), color=vec(0.7, 0.7, 0.7))
wing_right = box(pos=vec(2, -0.1, -1.8), size=vec(4, 0.05, 1.2), color=vec(0.7, 0.7, 0.7))

engine_left = cylinder(pos=vec(-1.2, -0.2, -1.2), axis=vec(0, 0, -1.2), radius=0.18, color=color.white)
engine_right = cylinder(pos=vec(1.2, -0.2, -1.2), axis=vec(0, 0, -1.2), radius=0.18, color=color.white)
tail_horizontal = box(pos=vec(0, 0, -3.6), size=vec(2, 0.04, 0.6), color=color.red)
tail_vertical = box(pos=vec(0, 0.4, -3.6), size=vec(0.04, 0.8, 0.6), color=color.red)

parts = [body, nose, win, wing_left, wing_right, engine_left, engine_right, tail_horizontal, tail_vertical]
airplane = compound(parts, make_trail=True, trail_type="curve", trail_color=color.yellow, trail_radius=0.08, retain=150)

airplane.pos = vec(0, 0, 0)
speed = 0.3  

airplane.pos = vector(0, 0, 0)
speed = 0.25

while True:
    rate(60) 
    
    k = keysdown() 
    
    if 'up' in k:
        airplane.pos.y += 0.1
    if 'down' in k:
        airplane.pos.y -= 0.1
    if 'left' in k:
        airplane.pos.x -= 0.1
    if 'right' in k:
        airplane.pos.x += 0.1
