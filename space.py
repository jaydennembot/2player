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
border = pygame.Rect(width//2-10,0,20,height)
space=pygame.image.load("space.jpg")
space=pygame.transform.scale(space,(width,height))

def draw(r1,v1,rbullets,vbullets):
    screen.blit(space,(0,0))
    pygame.draw.rect(screen,"blue",border)
    # pygame.draw.rect(screen,"white",r1)
    # pygame.draw.rect(screen,"white",v1)
    screen.blit(vampire,(v1.x-40,v1.y))
    screen.blit(robot,(r1.x-40,r1.y))
    for i in rbullets:
        pygame.draw.rect(screen,"grey",i)
    for i in vbullets:
        pygame.draw.rect(screen,"red",i)
def handlebullets(r1,v1,rbullets,vbullets):
    for i in rbullets:
        i.x-=10
        if i.x <0:
            rbullets.remove(i)
    for i in vbullets:
        i.x+=10
        if i.x >width:
            vbullets.remove(i)


    




def movement(r1,v1,button):
    # print(button)
    if button[pygame.K_w]and v1.y>0:
        v1.y-=10
    if button[pygame.K_a]and v1.x>0 :
        v1.x-=10
    if button[pygame.K_s]and v1.y<height-v1.height:
        v1.y+=10
    if button[pygame.K_d]and v1.x<border.x-v1.width:
        v1.x+=10
        print("hello")
    if button[pygame.K_UP]and r1.y>0:
        r1.y-=10
    if button[pygame.K_DOWN]and r1.y<height-r1.height:
        r1.y+=10
    if button[pygame.K_LEFT]and r1.x>border.x+border.width:
        r1.x-=10
    if button[pygame.K_RIGHT]and r1.x<width-r1.width:
        r1.x+=10
    


def main():
    r1=pygame.Rect(rx,ry,80,140)
    v1=pygame.Rect(vx,vy,80,140)
    rbullets=[]
    vbullets=[]
    while True:
    
        draw(r1,v1,rbullets,vbullets)
        for i in pygame.event.get():
            
            if i.type == pygame.QUIT :
                pygame.quit()
            if i.type== pygame.KEYDOWN:
                if i.key == pygame.K_LSHIFT:
                    b=pygame.Rect(v1.x-50,v1.y+50,50,15)
                    vbullets.append(b)
                if i.key == pygame.K_RSHIFT:
                    b=pygame.Rect(r1.x-50,r1.y+50,50,15)
                    rbullets.append(b)
        button=pygame.key.get_pressed()
        print(button)
        movement(r1,v1,button)
        handlebullets(r1,v1,rbullets,vbullets)

        pygame.display.update()





main()

