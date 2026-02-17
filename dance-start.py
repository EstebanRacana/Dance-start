import pygame,random,sys
width=800
height=600
WHITE=(0,0,0)
pygame.init()
screen=pygame.display.set_mode((width,height))
background=pygame.image.load("background.png").convert()
background=pygame.transform.scale(background,(width,height))
clock=pygame.time.Clock()
state="menu,game"
done=False
def begin_start():
    screen.fill(WHITE)
    font=pygame.font.SysFont("Arial",50)
    title=font.render("Dance-Start",True,(255,255,255))
    screen.blit(title,(250,200))

    small_font=pygame.font.SysFont("Arial",30)
    message=small_font.render("Presiona ESPACIO para continuar",True,(180,180,180))
    screen.blit(message,(200,350))

def start_game():
    screen.fill(WHITE)
    font=pygame.font.SysFont("Arial",50)
    title=font.render("¡A bailar!",True,(0,0,0))
    screen.blit(title,(250,200))
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==pygame.KEYDOWN:
            if state=="menu" and event.key==pygame.K_SPACE:
                state="game"
            if state=="game" and event.key==pygame.K_ESCAPE:
                state="menu"
    if state=="menu":
        begin_start()
    elif state=="game":
        start_game()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()