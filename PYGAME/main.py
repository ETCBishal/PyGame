import pygame
from pygame.locals import *
import random
pygame.init()

pygame.mixer.init()

screenWidth = 950
screenHeight = 500

bg_img = pygame.image.load('image/bg.jpg')
bg_img = pygame.transform.scale(bg_img,(screenWidth,screenHeight))

# colours
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
gold = (255, 215, 0)
yellow = (253,184,19)
darkBlue = "#0CA6F5"
pink = "#FFC0CB"



gameWindow = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("SnakeGame")
clock = pygame.time.Clock()
pygame.display.update()

FPS = 45

font = pygame.font.SysFont("comicsansms", 35)


def displayText(color, text, x, y):
    showFont = font.render(text, True, color)
    gameWindow.blit(showFont, [x, y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcomeScreen():
    exitGame = False
    while not exitGame:
        gameWindow.fill(pink)
        displayText(black,"-By Bishal jasiwal",20,20)
        displayText(yellow,"Welcome :D",400,170)
        displayText(red,"To",467,220)
        displayText(darkBlue,"Snake Game",383,270)
        displayText(green,"START : Space Bar",630,450)
        displayText(red,"Quit : q",10,450)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.load("bg.mp3")
                pygame.mixer.music.play()
                pygame.mixer.music.stop()
                exitGame = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.mixer.music.load("bg.mp3")
                    pygame.mixer.music.play()
                    pygame.mixer.music.stop()
                    exitGame = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("bg.mp3")
                    pygame.mixer.music.play()
                    gameWindow.blit(bg_img,(0,0))
                    gameloop()

        pygame.display.update()
        clock.tick(FPS)


def gameloop():

    # gameSpecific Variables
    gameOver = False
    exitGame = False
    score = 500

    snk_list = []
    snk_length = 1

    init_velocity = 7
    Xvelocity = 0
    Yvelocity = 0

    snake_y = random.randint(100, screenHeight/2)
    snake_x = random.randint(100, screenWidth/2)
    snake_size = 25

    # food
    food_x = random.randint(150, screenWidth/2)
    food_y = random.randint(150, screenHeight/2)

    with open("high_score.txt","r") as f:
        highScore = f.read()

    while not exitGame:
        if gameOver:
            with open("high_score.txt","w") as f:
                f.write(str(highScore))
            pygame.mixer.music.stop()
            gameWindow.fill(darkBlue)
            displayText(red, "Game Over!", 400, 190)
            displayText(red, "Press", 300, 250)
            displayText(green, "\"Enter\"", 410 , 250)
            displayText(yellow, "To Continue...", 550, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitGame = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load("bg.mp3")
                        pygame.mixer.music.play()
                        gameWindow.blit(bg_img,(0,0))
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitGame = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        Xvelocity = init_velocity
                        Yvelocity = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        Xvelocity = -init_velocity
                        Yvelocity = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        Yvelocity = init_velocity
                        Xvelocity = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        Yvelocity = -init_velocity
                        Xvelocity = 0

            snake_x += Xvelocity
            snake_y += Yvelocity

            if abs(snake_x-food_x) < 15 and abs(snake_y-food_y) < 15:
                score += 1
                food_x = random.randint(0, 900)
                food_y = random.randint(0, 470)
                snk_length += 5
                if score>int(highScore):
                    highScore = score
                

            gameWindow.fill(black)
            gameWindow.blit(bg_img,(0,0))

            displayText(gold, str(f"Score : {score}"), 15, 10)            
            displayText(gold, str(f"Hi Score : {str(highScore)}"), 230, 10)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            pygame.draw.circle(gameWindow, red, [food_x, food_y], 12, 0)

            plot_snake(gameWindow, green, snk_list, snake_size)

            if snake_x < 0 or snake_x > screenWidth or snake_y < 0 or snake_y > screenHeight:
                pygame.mixer.music.stop()
                gameOver = True

            if head in snk_list[:-1]:
                pygame.mixer.music.stop()
                gameOver = True

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()


welcomeScreen()
