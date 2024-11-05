import math
import random
import pygame
#constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 2
ENEMY_SPEED_Y = 20
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27
#initialize pygame
pygame.init()
#initialize the mixer for sounds
pygame.mixer.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#background
background = pygame.image.load('background.png')
#caption and icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
#load sounds
bullet_sound = pygame.mixer.Sound('bullet.wav')
explosion_sound = pygame.mixer.Sound('explosion.wav')
pygame.mixer.music.load('background.mp3') #load background music
pygame.mixer.music.play(-1) # play background music in a loop
#player
playerImg = pygame.image.load('player.png')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0
#enemy
enemyImg = []
enemyX =[]
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for _i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)
#bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = PLAYER_START_Y
bulletX_change = 0
bulletY_change = BULLET_SPEED_Y
bullet_state = "ready"
#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 64)
def show_score(x, y):
    #display the current score on the screen
    score = font.render("Score :"+str(score_value), True, (225, 225, 225))
    screen.blit(score, (x,y))
def game_over_text():
    #dsiplay the game over text
    over_text= over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
def player(x, y):
    #draw the player on the screen
    screen.blit(playerImg, (x,y))
    
