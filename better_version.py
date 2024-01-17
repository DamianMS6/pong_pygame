import pygame as py
import sys

py.init()
clock = py.time.Clock()

screen_width = 1280
screen_height = 960
screen = py.display.set_mode((screen_width,screen_height))
py.display.set_caption("Depression")


ball = py.Rect(screen_width/2,screen_height/2,10,10)
player = py.Rect(screen_width - 30, screen_height/2 - 70, 10, 140)
opponent = py.Rect(40, screen_height/2 - 70, 10, 140)

ball_speed_x = 7
ball_speed_y = 7



while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()


    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <=0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <=0 or ball.right >= screen_width:
        ball_speed_x *= -1

    py.draw.rect(screen,'aliceblue',player)
    py.draw.rect(screen, 'aliceblue', opponent)
    py.draw.rect(screen, 'aliceblue', ball)
    #py.draw.aaline(screen,'aliceblue', (screen_width/2,0), (screen_width/2, screen_height))



    py.display.update()
    screen.fill((0,0,0))
    clock.tick(60)