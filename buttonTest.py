#Tutorial: https://www.youtube.com/watch?v=G8MYGDf_9ho


import pygame
import button


HEIGHT = 800
WIDTH = 1200

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Button Demo")

#load in images

image1 = pygame.image.load("button1.png").convert_alpha()
image2 = pygame.image.load("button2.png").convert_alpha()



#Create button instances
start_button = button.Button(100, 200, image1, 0.8)
exit_button = button.Button(700, 200, image2, 0.8)

run = True

while run:

    screen.fill((202, 228, 241))
    

    if start_button.draw(screen):
        print("BUTTON 1")
    if exit_button.draw(screen):
        # run = False if you have this, one button will end the game
        print("Button 2")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()


pygame.quit()

