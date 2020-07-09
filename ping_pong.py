#Imports
import math, random, time
import pygame
import tkinter as tk
from tkinter import messagebox

#General setup
pygame.init()
clock = pygame.time.Clock()

#Display setup
width = 1200                #display width
height = 500                #display height
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Ping-Pong')

#Units' attributes
r_w = 20                            #racket width
r_h = 100                           #racket height
r_x_1 = 0                           #racket_1 x
r_x_2 = width-r_w                   #racket_2 x
r_y_1 = height//2 - r_h//2          #racket_1 y
r_y_2 = height//2 - r_h//2          #racket_2 y
ball_speed_x = random.randint(7,10) #ball x speed
ball_speed_y = random.randint(7,10) #ball y speed
r_speed_1 = 5                       #racket_1 move speed
r_speed_2 = ball_speed_y            #racket_2 move speed

#Game units
racket_1 = pygame.Rect((r_x_1, r_y_1), (r_w, r_h))
racket_2 = pygame.Rect((r_x_2, r_y_2), (r_w, r_h))
circle = pygame.Rect((width//2, height//2), (20, 20))

#Colors setup
blue = ((0,0,255))
green = ((0,255,0))
red = ((255,0,0))
white = ((255,255,255))
black = ((0,0,0))

#Score
player_score = 0
opponent_score = 0
game_font = pygame.font.Font('freesansbold.ttf', 35)

#Ball
class Ball:
    def __init__(self, surface, color, shape):
        self.surface = surface
        self.color = color
        self.shape = shape

    def draw(self, surface, color, shape):
        pygame.draw.ellipse(surface, color, shape)

    def move(self, circle):
        circle.x -= ball_speed_x
        circle.y += ball_speed_y
        return circle.x, circle.y

    def collision(self, circle):
        global ball_speed_x, ball_speed_y, player_score, opponent_score
        if circle.top <= 0 or circle.bottom >= height:
            ball_speed_y *= -1
        if circle.left + abs(ball_speed_x) < r_w:
            opponent_score += 1
            reset(circle)
        if circle.right - abs(ball_speed_x) > width-r_w:
            player_score += 1
            reset(circle)
        if circle.colliderect(racket_1) or circle.colliderect(racket_2):
            ball_speed_x *= -1

#Player
class Player:
    def __init__(self, surface, color, shape):
        self.surface = surface
        self.color = color
        self.shape = shape

    def draw(self, surface, color, shape):
        pygame.draw.rect(surface, color, shape)

#Opponent
class Opponent(Player):
    def move(self, circle):
        if racket_2.centery < circle.y:
            racket_2.top += r_speed_2
        if racket_2.centery > circle.y:
            racket_2.bottom -= r_speed_2
        if racket_2.top <= 0:
            racket_2.top = 0
        if racket_2.bottom >= height:
            racket_2.bottom = height


#Remap ball speed
def ball_speed():
    global ball_speed_x, ball_speed_y

#Check if exit
def check_exit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            message_box()
            pygame.display.quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        message_box()
        pygame.display.quit()

#Restart the ball
def reset(circle):
    global ball_speed_x, ball_speed_y
    circle.center = (width//2, height//2)
    ball_speed_x *= random.choice((1, -1))
    ball_speed_y *= random.choice((1, -1))

#Show score at the top of the screen
def show_score(keyword):
    if keyword == 1:
        win.blit(game_font.render(f'{player_score}', False, blue), (width//2-50, 30))
    if keyword == 2:
        win.blit(game_font.render(f'{opponent_score}', True, red), (width//2+50, 30))
    win.blit(game_font.render(f':', False, white), (width//2+5, 28))

#"Try again" window
def message_box():
    global player_score, opponent_score
    root = tk.Tk()
    root.withdraw()
    messagebox = tk.messagebox.askyesno('Game over', 'Try again?', icon='question')
    if messagebox == True:
        reset(circle)
        player_score = 0
        opponent_score = 0
        main()
    else:
        root.destroy()


def main():
    ball_speed()
    while True:
        check_exit()            #checks if the game was stopped
        win.fill(black)         #fills the window with certain color

        #Player animation
        player = Player(win, blue, racket_1)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and racket_1.y >= 0:
            racket_1.y -= r_speed_1
        if keys[pygame.K_DOWN] and racket_1.y <= height-r_h:
            racket_1.y += r_speed_1
        player.draw(player.surface, player.color, player.shape)

        #Opponent animation
        opponent = Opponent(win, red, racket_2)
        opponent.move(circle)
        opponent.draw(opponent.surface, opponent.color, opponent.shape)

        #Ball animation
        ball = Ball(win, white, circle)
        ball.move(circle)
        ball.collision(circle)
        ball.draw(ball.surface, ball.color, ball.shape)

        #Score showing
        show_score(1)
        show_score(2)

        #Display updating
        pygame.display.flip()
        clock.tick(60)

main()
