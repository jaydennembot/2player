import pygame,pyautogui
import random
pygame.init()

print(pyautogui.size())
width,height=pyautogui.size()
#width,height=600,600
screen=pygame.display.set_mode((width,height))

pygame.display.set_caption("space invasion")
vampire=pygame.transform.flip(pygame.image.load("vampire.png"),True,False)
vampire=pygame.transform.scale(vampire,(160,160))
robot=pygame.image.load("robot.png")
robot=pygame.transform.scale(robot,(160,160))
rx,ry=width-220,height//2
vx,vy=120,height//2
space=pygame.image.load("space.jpg")
space=pygame.transform.scale(space,(width,height))
r1=pygame.Rect(rx,ry,120,140)
v1=pygame.Rect(vx,vy,120,140)
while True:
   
    screen.blit(space,(0,0))
   
    pygame.draw.rect(screen,"white",r1)
    pygame.draw.rect(screen,"white",v1)
    screen.blit(vampire,(v1.x,v1.y))
    screen.blit(robot,(r1.x,r1.y))
    for i in pygame.event.get():
        print (i)
        if i.type == pygame.QUIT :
            pygame.quit()
    

    pygame.display.update()
