import pygame as py
import random

class Pong():
     def __init__(self, pos, up_key, down_key):
        self.y_dir = SCREEN_HEIGHT/2
        self.pos = pos
        self.up_key = up_key
        self.down_key = down_key

     def draw_pong(self):
        self.player = py.Rect(self.pos,self.y_dir,15,80)
        py.draw.rect(screen, 'aliceblue', self.player)

     def movement(self):
        keys = py.key.get_pressed()
        if keys[self.up_key]:
            if self.player.top != 0:
                self.y_dir -= 6
            else:
                print("stopped")
        if keys[self.down_key]:
            if self.player.bottom <= 600:
                self.y_dir += 6


class Ball():
    def __init__(self):
        self.ball_pos_y = SCREEN_HEIGHT/2
        self.ball_pos_x = SCREEN_WIDTH/2
        self.speed_x = 5
        self.speed_y = 5


    def draw_ball(self):

        self.ball = py.Rect(self.ball_pos_x,self.ball_pos_y,10,10)
        py.draw.rect(screen, 'aliceblue', self.ball)

    def movement(self):

        if self.ball.bottom >= SCREEN_HEIGHT or self.ball.top <= 0:
            self.speed_y *= -1

        #if self.ball.right >= SCREEN_WIDTH or self.ball.left <= 0:
        #    self.speed_x *= -1

        self.ball_pos_x += self.speed_x
        self.ball_pos_y += self.speed_y


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

player1 = Pong(30, py.K_TAB, py.K_CAPSLOCK)
player2 = Pong(SCREEN_WIDTH - 40, py.K_UP, py.K_DOWN)
#player3 = Pong(SCREEN_WIDTH/2, py.K_w,py.K_s )


ball = Ball()
py.init()
clock = py.time.Clock()

font = py.font.Font(None, 35)

screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
py.display.set_caption("Pong")
score_left = 0
score_right = 0

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()

    screen.fill((0, 0, 0))
    text_score_left = font.render(str(score_right), True, 'aliceblue')
    text_score_right = font.render(str(score_left), True, 'aliceblue')
    screen.blit(text_score_left, (25,20))
    screen.blit(text_score_right, (750,20))

    player1.movement()
    player1.draw_pong()

    player2.movement()
    player2.draw_pong()

    #player3.movement()
    #player3.draw_pong()

    ball.draw_ball()

    if ball.ball_pos_x >= SCREEN_WIDTH + 10:
        score_right += 1
        print('goal')
        py.time.delay(1500)
        ball.ball_pos_x = SCREEN_WIDTH/2
        ball.ball_pos_y = SCREEN_HEIGHT/2

    if ball.ball_pos_x <= 0 - 20:
        score_left += 1
        print('goal')
        py.time.delay(1500)
        ball.ball_pos_x = SCREEN_WIDTH/2
        ball.ball_pos_y = SCREEN_HEIGHT/2

    if ball.ball.colliderect(player1.player):
        ball.speed_x *= -1
    if ball.ball.colliderect(player2.player):
        ball.speed_x *= -1

    ball.movement()
    py.display.update()
    clock.tick(60)











