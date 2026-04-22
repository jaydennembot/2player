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

def draw(r1,v1):
    screen.blit(space,(0,0))
   
    # pygame.draw.rect(screen,"white",r1)
    # pygame.draw.rect(screen,"white",v1)
    screen.blit(vampire,(v1.x-40,v1.y))
    screen.blit(robot,(r1.x-40,r1.y))

def movement(r1,v1,button):
    # print(button)
    if button == pygame.K_w:
        v1.y-=10
    if button == pygame.K_a:
        v1.x-=10
    if button == pygame.K_s:
        v1.y+=10
    if button == pygame.K_d:
        v1.x+=10
        print("hello")
    if button == pygame.K_UP:
        r1.y-=10
    if button == pygame.K_DOWN:
        r1.y+=10
    if button == pygame.K_LEFT:
        r1.x-=10
    if button == pygame.K_RIGHT:
        r1.x+=10
    


def main():
    r1=pygame.Rect(rx,ry,80,140)
    v1=pygame.Rect(vx,vy,80,140)
    while True:
    
        draw(r1,v1)
        for i in pygame.event.get():
            
            if i.type == pygame.QUIT :
                pygame.quit()
        button=pygame.key.get_pressed()
        print(button)
        movement(r1,v1,button)
        

        pygame.display.update()

main()