from helpers import *
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

# circle radius
RADIUS = 80;

start = (100, 600)
end = (900, 100)
circles = [
(400,200),
(290, 430),
(150,300),
(700, 200),
(500,500),
(850, 450)
]

getBorderLines(circles)

# Import a library of functions called 'pygame'
import pygame
from math import pi
 
# Initialize the game engine
pygame.init()
 

 
# Set the height and width of the screen
size = [1000, 800]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Example code for the draw module")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
     
    # Clear the screen and set the screen background
    screen.fill(WHITE)
 
    # Draw on the screen a GREEN line from (0,0) to (50.75) 
    # 5 pixels wide.
    #pygame.draw.line(screen, GREEN, [0, 0], [50,30], 5)

    for line in getBorderLines(circles):
        pygame.draw.line(screen, GREEN, line[0], line[1], 5)
        
 
     
    # Draw a solid rectangle
    #pygame.draw.rect(screen, BLACK, [start[0] + 5, start[1] + 5, start[0] - 5, start[1] - 5])
    pygame.draw.rect(screen, GREEN, [start[0] - 10, start[1] - 10, 20, 20])
    pygame.draw.rect(screen, RED, [end[0] - 10, end[1] - 10, 20, 20])
    #pygame.draw.rect(screen, BLACK, [1, 100, 30, 200])
    
    # Draw circles
    for pos in circles:
        pygame.draw.circle(screen, BLUE, [pos[0], pos[1]], RADIUS)
    
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()