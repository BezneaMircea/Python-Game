import pygame

from RectButton import RectButton




# Can be changed depending on what resolution we want
screenWidth = 1280
screenHeight = 720

pygame.init()

screen = pygame.display.set_mode((screenWidth, screenHeight))

running = True

buttonPath = "Untitled.png"
backgroundPath = "background.jpg"

backgroundImg = pygame.image.load(backgroundPath)

xPos = screenHeight - (screenHeight) / 10 - 50
yPos = (screenWidth) / 2 - 100


while running:

    button = RectButton(screen=screen, xPos=xPos, yPos=yPos, path=buttonPath)
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        
  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = False
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if(button.isPressed(pygame.mouse.get_pos())):
                    running = False
    
    screen.blit(backgroundImg, (0, 0))
    button.drawButton()

    pygame.display.flip()
        
             
pygame.quit()