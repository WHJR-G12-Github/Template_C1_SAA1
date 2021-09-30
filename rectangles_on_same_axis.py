# Importing 'pygame'
import pygame

# Initializing 'pygame'
pygame.init()

# Creating game window of width 400 and height 600
screen = pygame.display.set_mode((400,600))

# Setting the title of the game
pygame.display.set_caption("Rectangles on the same axis")

# Creating BLUE color using RGB combinations and naming it as 'BLUE'
BLUE=(0,0,255)
# Creating a rectangle at the coordinates 200,200 with width and height
blue_rect=pygame.Rect(200,200,30,30)
# Drawing the 'blue_rect' rectangle in the screen in BLUE color
pygame.draw.rect(screen,BLUE,blue_rect)

# Creating WHITE color using RGB combinations and naming it as 'WHITE'
WHITE=(255,255,255)
# Creating and displaying WHITE rectangle
white_rect=pygame.Rect(200,230,30,30)
pygame.draw.rect(screen,WHITE,white_rect)

# Creating PINK color using RGB combinations and naming it as 'PINK'
PINK=(255,0,104)
# Creating and displaying WHITE rectangle
pink_rect=pygame.Rect(200,260,30,30)
pygame.draw.rect(screen,PINK,pink_rect)

# Updating the screen display
pygame.display.update()
