#pip install ursina

from ursina import *


app= Ursina()

window.color=color.violet

table= Entity(
    model='cube', 
    color= color.black,
    scale=(2,1,3),
    rotation=(90,0,0)
)

ball = Entity(
    model="sphere",
    z=-1,
    collider="sphere",
    scale=0.1
)

player1= Entity(
    model="cube",
    collider="box",
    position=(0,-1.5,-1),
    scale=(0.5,0.1,1),
    color=color.pink
)

camera.orthographic= True
camera.fov=4

player2= duplicate(player1, y=1.5)


speed_x=1
speed_y=1

label1=Text(
    text=f'Points: {0}',
    color=color.black,
    position=(0,0.45),
    origin=(0,0),
    scale=1.5
)

label2= duplicate(label1, y=-0.45)

points1=0
points2=-1
def update():
    global speed_x, speed_y, points1, points2
    label1.text=f'Point: {points1}'
    label2.text=f'Point: {points2}'

    ball.x+=speed_x*time.dt
    ball.y+=speed_y*time.dt
    if abs(ball.x)>1:
        speed_x=-speed_x

    if ball.y>1.45:
        ball.x=0
        ball.y=0
        speed_x=1
        speed_y=1
        points2+=1

    if ball.y<-1.45:
        ball.x=0
        ball.y=0
        speed_x=1
        speed_y=1
        points1+=1

    if player1.x<0.75:
        player1.x+=held_keys['d']*time.dt
    if player1.x>-0.75:
        player1.x-=held_keys['a']*time.dt
    if player2.x<0.75:
        player2.x+=held_keys['right arrow']*time.dt
    if player2.x>-0.75:
        player2.x-=held_keys['left arrow']*time.dt

    if ball.intersects().hit:
        speed_y=-speed_y
        speed_x*=1.1
        speed_y*=1.1

    if player1.x==0.75:
        player1.x=0.75




app.run()

