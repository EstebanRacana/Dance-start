import pygame,random,sys

width=800  
height=600 
BLACK=(0,0,0)  
pygame.mixer.init()
songs=[
    {"name":"Cancion 1","file":"music/A Rising Wave - Jeremy Blake.mp3"},
    {"name":"Cancion 2","file":"music/The Machines Dream - South London HiFi.mp3"}
    
]
current_song=None
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
score=0
combo=0
notes=[]
note_speed=4
def spawn_note():
    lane = random.randint(0, 2)
    colors = [(255, 50, 50), (50, 100, 255), (255, 255, 50)]
    lane_positions = {0: 210, 1: 320, 2: 430}  # Centros de los carriles
    
    note = {
        "lane": lane,
        "x": lane_positions[lane],
        "y": 0,  # Empieza desde arriba
        "color": colors[lane],
        "hit": False
    }
    notes.append(note)
def draw_lanes():
    pygame.draw.line(screen, (255, 80, 80), (210, 0), (210, 500), 6)
    

    pygame.draw.line(screen, (80, 150, 255), (320, 0), (320, 500), 6)
    

    pygame.draw.line(screen, (255, 255, 80), (430, 0), (430, 500), 6)

def draw_hit_line():
    hit_zone = pygame.Surface((500, 60))
    hit_zone.set_alpha(80)
    hit_zone.fill((255, 255, 255))
    screen.blit(hit_zone, (130, 440))

    pygame.draw.line(screen, (255, 255, 255), (130, 440), (630, 440), 3)
    pygame.draw.line(screen, (255, 255, 255), (130, 500), (630, 500), 3)

def update_notes():
    global combo, score
    for note in notes[:]:
        note["y"] += note_speed
        
        if note["y"] > 520 and not note["hit"]:
            notes.remove(note)
            combo = 0
            print("❌ MISS!")
        
        elif note["y"] > height and note["hit"]:
            notes.remove(note)

def draw_notes():
    for note in notes:
        if not note["hit"]:
            pygame.draw.circle(screen, note["color"], (note["x"], int(note["y"])), 25)

            pygame.draw.circle(screen, (255, 255, 255), (note["x"], int(note["y"])), 25, 4)
            
            pygame.draw.circle(screen, (255, 255, 255), (note["x"], int(note["y"])), 10)

def check_hit(lane):
    global score, combo
    lane_map = {'a': 0, 's': 1, 'd': 2}
    lane_num = lane_map.get(lane, -1)
    
    for note in notes:
        if note["lane"] == lane_num and 420 < note["y"] < 520 and not note["hit"]:
            note["hit"] = True
            score += 100 + (combo * 10)
            combo += 1
            print(f"✅ HIT! +{100 + (combo * 10)} - Combo: {combo}x")
            return True
    
    combo = 0
    print("❌ Miss - combo perdido")
    return False


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
    draw_lanes()
    draw_song_display()
    draw_hit_line()
    draw_notes()

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

def play_random_song():
    global current_song
    current_song=random.choice(songs)
    pygame.mixer.music.load(current_song["file"])
    pygame.mixer.music.play(-1)
    print(f"Reproduciendo: {current_song['name']}")
def draw_song_display():
    if current_song:
        song_box=pygame.Surface((400,60))
        song_box.set_alpha(180) 
        song_box.fill((20, 20, 40))
        screen.blit(song_box, (width//2 - 200, 20))
        
        pygame.draw.rect(screen, (255, 100, 255), (width//2 - 200, 20, 400, 60), 3)
        
        font = pygame.font.SysFont("Arial", 28, bold=True)
        text = font.render(f"♫ {current_song['name']}", True, (255, 255, 255))
        text_rect = text.get_rect(center=(width//2, 50))
        screen.blit(text, text_rect)
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
                    check_hit('a')
                    print("Bailas con A - ROJO")
                if event.key == pygame.K_s:
                    button_states['s'] = True
                    check_hit('s')
                    print("Bailas con S - AZUL")
                if event.key == pygame.K_d:
                    button_states['d'] = True
                    check_hit('d')
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
    if state=="game" and not show_start:
            update_notes()
            if random.randint(1, 40) == 1:
                spawn_note()
    if event.type==pygame.KEYDOWN:
        if state=="menu" and event.key==pygame.K_SPACE:
            state="game"
            start_time=pygame.time.get_ticks()
            show_start=True
            play_random_song()
      
    if state=="game" and start_time is not None:
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000 
        if elapsed_time >= 3: 
            show_start=False 

    if state=="game" and not pygame.mixer.music.get_busy():
        play_random_song()

    if state=="menu":
        begin_start()  
    elif state=="game":
        start_game() 
    
    pygame.display.flip() 
    clock.tick(60) 

pygame.quit() 