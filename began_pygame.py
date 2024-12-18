import pygame  

pygame. init()

pygame.display.set_mode((100,200))

done=False

while not done :
    for event in pygame.event.get():
        if event.type==event.QUIT():
            pygame.quit()

    pygame.display.flip()
