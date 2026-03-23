#IMPORTANT READ:
#This game is only inspiration, the author for the songs it's only for the game and don't have prices.
#It's just for fun and creative, if you use this project for one reason, for example to have got businnes, you got problems.
#This project it's only a videogame to create for fun, not business.
#Thank you for reading, goodbye!
#AUTHOR FOR THE SONGS: Library of Youtube. The songs only use for the videogame.
import pygame,random,sys

width=800  
height=600 
BLACK=(0,0,0)  
HORIZON_Y = 280  
LANE_X_TARGETS = [280, 400, 520] 
HIT_ZONE_Y = 530
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

button_blue= pygame.image.load("button_blue.png").convert_alpha() 
button_blue=pygame.transform.scale(button_blue,(80,80))  

button_red=pygame.image.load("button_red.png").convert_alpha()  
button_red=pygame.transform.scale(button_red,(80,80))

button_yellow=pygame.image.load("button_yellow.png").convert_alpha()
button_yellow=pygame.transform.scale(button_yellow,(80,80))
#----------------------------------------------------------------
button_red_pressed=pygame.image.load("button_red_pressed.png").convert_alpha()
button_red_pressed=pygame.transform.scale(button_red_pressed,(85,85))
button_red_pressed.set_colorkey((0,0,0))

button_blue_pressed=pygame.image.load("button_blue_pressed.png").convert_alpha()
button_blue_pressed=pygame.transform.scale(button_blue_pressed,(85,85))
button_blue_pressed.set_colorkey((0,0,0))

button_yellow_pressed=pygame.image.load("button_yellow_pressed.png").convert_alpha()
button_yellow_pressed=pygame.transform.scale(button_yellow_pressed,(85,85))
button_yellow_pressed.set_colorkey((0,0,0))


button_states = {
    'a': False,
    's': False,
    'd': False
}
score=0
combo=0
feedback_message = ""
feedback_timer = 0  
feedback_color = (255, 255, 255) 
notes=[]
note_speed=4

def spawn_note():
    lane = random.randint(0, 2)
    colors = [(255, 50, 50), (50, 150, 255), (255, 255, 50)]
    
    note = {
        "lane": lane,
        "x": 400,      
        "y": 280,        
        "color": colors[lane],
        "hit": False
    }
    notes.append(note)
def draw_lanes():

    lane_colors = [(200, 0, 0), (0, 100, 255), (200, 200, 0)]
    for i in range(3):
        pygame.draw.line(screen, lane_colors[i], (400, HORIZON_Y), (LANE_X_TARGETS[i], 600), 5)
def draw_hit_line():
  pass

def update_notes():
    global combo, score

    HORIZON_Y = 280
    LANE_X_TARGETS = [280, 400, 520] 
    HIT_ZONE_Y = 530 

    for note in notes[:]:
        note["y"] += note_speed
        

        progress = (note["y"] - HORIZON_Y) / (HIT_ZONE_Y - HORIZON_Y)
        progress = max(0, progress)
        

        target_x = LANE_X_TARGETS[note["lane"]]
        note["x"] = 400 + (target_x - 400) * progress  
        
 
        if note["y"] > HIT_ZONE_Y + 50 and not note["hit"]:
            notes.remove(note)
            combo = 0
            print("❌ MISS CLICK")
        elif note["y"] > 600 and note["hit"]:
            notes.remove(note)
def draw_notes():
    for note in notes:
        if not note["hit"]:
            distancia_recorrida = note["y"] - HORIZON_Y
            progress = max(0, distancia_recorrida / 300)
            

            radius = int(8 + (24 * progress))
            

            pygame.draw.circle(screen, note["color"], (int(note["x"]), int(note["y"])), radius)
            

            pygame.draw.circle(screen, (255, 255, 255), (int(note["x"]), int(note["y"])), radius, 2)
            
            pygame.draw.circle(screen, (255, 255, 255), (int(note["x"]), int(note["y"])), radius // 3)

def check_hit(lane):
    global score, combo
    lane_map = {'a': 0, 's': 1, 'd': 2}
    lane_num = lane_map.get(lane, -1)
    
    for note in notes:
        if note["lane"] == lane_num and abs(note["y"] - HIT_ZONE_Y) < 40 and not note["hit"]:
            note["hit"] = True
            score += 100
            combo += 1
            print(f"🔥 GOOD CLICK! Combo: {combo}")
            return True
            
    print("💀 MISS CLICK (A destiempo)")
    combo = 0
    return False
   
def draw_feedback():
    global feedback_timer
    
    if feedback_timer > 0:
        alpha = min(255, feedback_timer * 8)
        
        font = pygame.font.SysFont("Arial", 60, bold=True)
        text = font.render(feedback_message, True, feedback_color)
        text_rect = text.rect(center=(width//2, 150))
        
        bg_surface = pygame.Surface((text.get_width() + 40, text.get_height() + 20))
        bg_surface.set_alpha(alpha // 2)
        bg_surface.fill((0, 0, 0))
        screen.blit(bg_surface, (text_rect.x - 20, text_rect.y - 10))
        

        text_surface = font.render(feedback_message, True, feedback_color)
        text_surface.set_alpha(alpha)
        screen.blit(text_surface, text_rect)
        
        feedback_timer -= 1 



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
    draw_feedback()
    if button_states['a']:
        screen.blit(button_red_pressed, (LANE_X_TARGETS[0] - 40, HIT_ZONE_Y - 40))
    else:
        screen.blit(button_red, (LANE_X_TARGETS[0] - 40, HIT_ZONE_Y - 40))
        
    if button_states['s']:
        screen.blit(button_blue_pressed, (LANE_X_TARGETS[1] - 40, HIT_ZONE_Y - 40))
    else:
        screen.blit(button_blue, (LANE_X_TARGETS[1] - 40, HIT_ZONE_Y - 40))
        
    if button_states['d']:
        screen.blit(button_yellow_pressed, (LANE_X_TARGETS[2] - 40, HIT_ZONE_Y - 40))
    else:
        screen.blit(button_yellow, (LANE_X_TARGETS[2] - 40, HIT_ZONE_Y - 40))

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
                if event.key == pygame.K_s:
                    button_states['s'] = True
                    check_hit('s')
                if event.key == pygame.K_d:
                    button_states['d'] = True
                    check_hit('d')
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                button_states['a'] = False
            if event.key == pygame.K_s:
                button_states['s'] = False
            if event.key == pygame.K_d:
                button_states['d'] = False
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