import pygame,random,sys
width=800
height=600
WHITE=(0,0,0)
pygame.init()
screen=pygame.display.set_mode((width,height))
background=pygame.image.load("background.png").convert_alpha()
background=pygame.transform.scale(background,(width,height))
background.set_alpha(128)
background_dance=pygame.image.load("background_start_game.png").convert_alpha()
background_dance=pygame.transform.scale(background_dance,(width,height))
clock=pygame.time.Clock()
state="menu"
done=False
show_start=True
start_time=None
def begin_start():
    screen.blit(background,(0,0))
    small_font=pygame.font.SysFont("Arial",32)
    message=small_font.render("Presiona ESPACIO para continuar",True,(255,255,255))
    message_rect=message.get_rect(center=(width/2,height/2+100))    
    screen.blit(message,(200,350))
class Button(pygame.sprite.Sprite):
    def _init__(self):
        super().__init__()
        self.image=pygame.image.load("button_red.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect=self.image.get_rect()

    def update(self):
        self.rect.y+=1
        if self.rect.y>height:
            self.rect.y=-10
            self.rect.x=random.randrange(900)
def logic():
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_a:
                print("¡Vamos a bailar!")
            if event.key==pygame.K_s:
                print("¡Sigue el ritmo!")
            if event.key==pygame.K_d:
                print("¡Muévete!")    
def start_game():
    global show_start
    screen.blit(background,(0,0))
    if show_start:
        font=pygame.font.SysFont("Arial",50)
        title=font.render("¡A bailar!",True,(255,255,255))
        title_rect=title.get_rect(center=(width/2,height/2))    
        screen.blit(title,title_rect)
    else:
        screen.blit(background_dance,(0,0))
        logic()

    
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==pygame.KEYDOWN:
            if state=="menu" and event.key==pygame.K_SPACE:
                state="game"
                start_time=pygame.time.get_ticks()
                show_start=True
            if state=="game" and event.key==pygame.K_ESCAPE:
                state="menu"
    if state=="game" and start_time is not None:
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000 
        if elapsed_time >= 3:
            show_start=False
    if state=="menu":
        begin_start()
    elif state=="game":
        start_game()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()