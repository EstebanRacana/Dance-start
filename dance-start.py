import pygame,random,sys

width=800  
height=600 
BLACK=(0,0,0)  

pygame.init()
screen=pygame.display.set_mode((width,height)) 


background=pygame.image.load("background.png").convert_alpha() 
background=pygame.transform.scale(background,(width,height)) 
background.set_alpha(128) 


background_dance=pygame.image.load("background_start_game.png").convert_alpha()
background_dance=pygame.transform.scale(background_dance,(width,height))

# Botones estaticos
button_blue= pygame.image.load("button_blue.png").convert_alpha() 
button_blue=pygame.transform.scale(button_blue,(80,80))  

button_red=pygame.image.load("button_red.png").convert_alpha()  
button_red=pygame.transform.scale(button_red,(80,80))

button_yellow=pygame.image.load("button_yellow.png").convert_alpha()
button_yellow=pygame.transform.scale(button_yellow,(80,80))
#----------------------------------------------------------------
button_red_pressed=pygame.image.load("button_red_pressed.png").convert_alpha()
button_red_pressed=pygame.transform.scale(button_red_pressed,(80,80))

button_blue_pressed=pygame.image.load("button_blue_pressed.png").convert_alpha()
button_blue_pressed=pygame.transform.scale(button_blue_pressed,(80,80))

button_yellow_pressed=pygame.image.load("button_yellow_pressed.png").convert_alpha()
button_yellow_pressed=pygame.transform.scale(button_yellow_pressed,(80,80))


button_states = {
    'a': False,
    's': False,
    'd': False
}

clock=pygame.time.Clock() 
state="menu" 
done=False  

start_time=None 
show_start=True  



def begin_start():
    screen.blit(background,(0,0))  
    small_font=pygame.font.SysFont("Arial",32)  
    message=small_font.render("Presiona ESPACIO para continuar",True,(255,255,255)) 
    message_rect=message.get_rect(center=(width/2,height/2+100))  
    screen.blit(message,message_rect) 


def start_game():
    global show_start  
    screen.blit(background_dance,(0,0))  
    
    if show_start:  
       
        font=pygame.font.SysFont("Arial",50)
        title=font.render("¡A bailar!",True,(255,255,255))
        title_rect=title.get_rect(center=(width/2,height/2))  
        screen.blit(title,title_rect) 
    else: 
        draw_game() 

def draw_game():
    screen.blit(background_dance,(0,0))

    if button_states['a']:
            screen.blit(button_red_pressed,(190,500))
    else:
        screen.blit(button_red,(190,500))
        
    if button_states['s']:
        screen.blit(button_blue_pressed,(300, 500))
    else:
        screen.blit(button_blue,(300, 500))
        
    if button_states['d']:
        screen.blit(button_yellow_pressed,(410,500))
    else:
        screen.blit(button_yellow,(410,500))


while not done:  
    
 
    for event in pygame.event.get(): 
        if event.type==pygame.QUIT: 
            done=True 
        
        if event.type==pygame.KEYDOWN: 
           
            if state=="menu" and event.key==pygame.K_SPACE:
                state="game" 
                start_time=pygame.time.get_ticks() 
                show_start=True 
            
            if state == "game" and not show_start:
                if event.key == pygame.K_a:
                    button_states['a'] = True
                    print("Bailas con A - ROJO")
                if event.key == pygame.K_s:
                    button_states['s'] = True
                    print("Bailas con S - AZUL")
                if event.key == pygame.K_d:
                    button_states['d'] = True
                    print("Bailas con D - AMARILLO")
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                button_states['a'] = False
                print("Frenas con A")
            if event.key == pygame.K_s:
                button_states['s'] = False
                print("Frenas con S")
            if event.key == pygame.K_d:
                button_states['d'] = False
                print("Frenas con D")
      
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