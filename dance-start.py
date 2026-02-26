import pygame,random,sys

#--------- CONFIGURACIÓN INICIAL ---------
width=800  # Ancho de la ventana en píxeles
height=600  # Alto de la ventana en píxeles
BLACK=(0,0,0)  # Color negro (nombre confuso, debería ser BLACK)

pygame.init()  # Inicializa todos los módulos de Pygame
screen=pygame.display.set_mode((width,height))  # Crea la ventana del juego

# CARGA Y PROCESA IMAGEN DE FONDO DEL MENÚ
background=pygame.image.load("background.png").convert_alpha()  # Carga imagen con transparencia
background=pygame.transform.scale(background,(width,height))  # Redimensiona al tamaño de ventana
background.set_alpha(128)  # Le da 50% de transparencia (0=invisible, 255=opaco)

# CARGA IMAGEN DE FONDO DEL JUEGO
background_dance=pygame.image.load("background_start_game.png").convert_alpha()
background_dance=pygame.transform.scale(background_dance,(width,height))

# CARGA IMÁGENES DE BOTONES (nombres intercambiados por error)
botton_blue= pygame.image.load("button_red.png").convert_alpha()  # Carga botón "rojo" pero lo llama blue
botton_blue=pygame.transform.scale(botton_blue,(80,80))  # Lo hace de 80x80 píxeles

botton_red=pygame.image.load("button_blue.png").convert_alpha()  # Carga botón "azul" pero lo llama red
botton_red=pygame.transform.scale(botton_red,(80,80))

botton_yellow=pygame.image.load("button_yellow.png").convert_alpha()
botton_yellow=pygame.transform.scale(botton_yellow,(80,80))
button_states = {
    'a': {'pressed': False},
    's': {'pressed': False},
    'd': {'pressed': False}
}
#--------- VARIABLES DE CONTROL DEL JUEGO ---------
clock=pygame.time.Clock()  # Controla los FPS (cuadros por segundo)
state="menu"  # Estado actual: puede ser "menu" o "game"
done=False  # Variable que controla el loop principal (False=sigue jugando)

start_time=None  # Guarda el momento en que empieza el juego (para el temporizador)
show_start=True  # Controla si muestra el texto "¡A bailar!" (True=mostrar, False=ocultar)
show_buttons=True  # Variable declarada pero no usada en el código
coord_x=10  # Coordenada X (no se usa actualmente)
coord_y=10  # Coordenada Y (no se usa actualmente)
x_speed=0  # Velocidad horizontal (no se usa actualmente)
y_speed=0  # Velocidad vertical (no se usa actualmente)

#--------- FUNCIONES ---------

# PANTALLA DE MENÚ INICIAL
def begin_start():
    screen.blit(background,(0,0))  # Dibuja el fondo del menú en posición (0,0)
    small_font=pygame.font.SysFont("Arial",32)  # Crea fuente Arial tamaño 32
    message=small_font.render("Presiona ESPACIO para continuar",True,(255,255,255))  # Crea texto blanco
    message_rect=message.get_rect(center=(width/2,height/2+100))  # Calcula posición centrada
    screen.blit(message,(200,350))  # Dibuja el texto (nota: ignora message_rect y usa coordenadas fijas)

# PANTALLA DEL JUEGO
def start_game():
    global show_start  # Permite modificar la variable show_start desde dentro de la función
    screen.blit(background_dance,(0,0))  # Dibuja el fondo
    
    if show_start:  # Si show_start es True...
        # Muestra el texto "¡A bailar!" durante 3 segundos
        font=pygame.font.SysFont("Arial",50)
        title=font.render("¡A bailar!",True,(255,255,255))
        title_rect=title.get_rect(center=(width/2,height/2))  # Centra el texto
        screen.blit(title,title_rect)  # Lo dibuja
    else:  # Después de 3 segundos...
        logic()  # Llama a la función logic() que maneja el juego
# LÓGICA DEL JUEGO (detecta teclas A, S, D)
def logic():
    global button_states
    base_y=500
    pressed_y=520
   # Dibuja botón azul (A) - se mueve si está presionado
    y_blue = pressed_y if button_states['a']['pressed'] else base_y
    screen.blit(botton_blue, (190, y_blue))
    
    # Dibuja botón rojo (S) - se mueve si está presionado
    y_red = pressed_y if button_states['s']['pressed'] else base_y
    screen.blit(botton_red, (300, y_red))
    
    # Dibuja botón amarillo (D) - se mueve si está presionado
    y_yellow = pressed_y if button_states['d']['pressed'] else base_y
    screen.blit(botton_yellow, (410, y_yellow))

    for event in pygame.event.get():  # Revisa todos los eventos
        if event.type==pygame.QUIT:  # Si cierran la ventana
            pygame.quit()
            sys.exit()
        
        if event.type==pygame.KEYDOWN:  # Si presionan una tecla
            if event.key==pygame.K_a:
                button_states['a']['pressed']=True #Marca presionado
                print("Bailas con A")
            if event.key==pygame.K_s:
                button_states['s']['pressed']=True #Marca presionado
                print("Bailas con S")
            if event.key==pygame.K_d:
               button_states['d']['pressed']=True #Marca presionado
               print("Bailas con D")
        
        if event.type==pygame.KEYUP:  # Si sueltan una tecla
            if event.key==pygame.K_a:
                button_states['a']['pressed']=False #Marca no presionado
                print("frenas con A")
            if event.key==pygame.K_s:
                button_states['a']['pressed']=False #Marca no presionado
                print("frenas con s")
            if event.key==pygame.K_d:
               button_states['a']['pressed']=False #Marca no presionado
               print("frenas con d")

#--------- LOOP PRINCIPAL DEL JUEGO (se ejecuta 60 veces por segundo) ---------
while not done:  # Mientras done sea False, sigue ejecutándose
    
    # MANEJO DE EVENTOS
    for event in pygame.event.get():  # Revisa todos los eventos (clicks, teclas, etc)
        if event.type==pygame.QUIT:  # Si cierran la ventana con la X
            done=True  # Sale del loop
        
        if event.type==pygame.KEYDOWN:  # Si presionan una tecla
            # Si están en el menú y presionan ESPACIO
            if state=="menu" and event.key==pygame.K_SPACE:
                state="game"  # Cambia al estado de juego
                start_time=pygame.time.get_ticks()  # Guarda el tiempo actual en milisegundos
                show_start=True  # Muestra el texto "¡A bailar!"
            
            # Si están en el juego y presionan ESC
            if state=="game" and event.key==pygame.K_ESCAPE:
                state="menu"  # Vuelve al menú
    
    # TEMPORIZADOR: Oculta "¡A bailar!" después de 3 segundos
    if state=="game" and start_time is not None:
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000  # Calcula segundos transcurridos
        if elapsed_time >= 3:  # Si pasaron 3 segundos o más
            show_start=False  # Oculta el texto
    
    # DIBUJA LA PANTALLA CORRESPONDIENTE SEGÚN EL ESTADO
    if state=="menu":
        begin_start()  # Dibuja el menú
    elif state=="game":
        start_game()  # Dibuja el juego
    
    pygame.display.flip()  # Actualiza toda la pantalla (muestra lo dibujado)
    clock.tick(60)  # Limita el juego a 60 FPS (frames por segundo)

pygame.quit()  # Cierra Pygame al salir del loop