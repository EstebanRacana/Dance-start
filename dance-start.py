import pygame,random,sys  # Importa librerías: pygame (juegos), random (números aleatorios), sys (salir del programa)

#--------- CONFIGURACIÓN INICIAL ---------
width=800  # Ancho de la ventana: 800 píxeles
height=600  # Alto de la ventana: 600 píxeles
BLACK=(0,0,0)  # Color negro en formato RGB (Red, Green, Blue)

pygame.init()  # Inicializa todos los módulos de Pygame (gráficos, sonido, eventos, etc)
screen=pygame.display.set_mode((width,height))  # Crea la ventana del juego de 800x600

# CARGA Y PROCESA IMAGEN DE FONDO DEL MENÚ
background=pygame.image.load("background.png").convert_alpha()  # Carga la imagen del menú con soporte de transparencia
background=pygame.transform.scale(background,(width,height))  # Redimensiona la imagen para que ocupe toda la ventana
background.set_alpha(128)  # Hace la imagen 50% transparente (0=invisible, 255=completamente opaco)

# CARGA IMAGEN DE FONDO DEL JUEGO
background_dance=pygame.image.load("background_start_game.png").convert_alpha()  # Carga el fondo con los 4 carriles de colores
background_dance=pygame.transform.scale(background_dance,(width,height))  # Lo ajusta al tamaño de la ventana

# ✅ CARGA BOTONES NORMALES PRIMERO (estado sin presionar)
botton_blue = pygame.image.load("button_blue.png").convert_alpha()  # Carga imagen del botón azul
botton_blue = pygame.transform.scale(botton_blue,(80,80))  # Lo redimensiona a 80x80 píxeles

botton_red = pygame.image.load("button_red.png").convert_alpha()  # Carga imagen del botón rojo
botton_red = pygame.transform.scale(botton_red,(80,80))  # 80x80 píxeles

botton_yellow = pygame.image.load("button_yellow.png").convert_alpha()  # Carga imagen del botón amarillo
botton_yellow = pygame.transform.scale(botton_yellow,(80,80))  # 80x80 píxeles

# ✅ CARGA BOTONES PRESIONADOS DESPUÉS (estado cuando el jugador presiona la tecla)
botton_red_pressed = pygame.image.load("button_red_pressed.png").convert_alpha()  # Versión "presionada" del botón rojo
botton_red_pressed = pygame.transform.scale(botton_red_pressed,(80,80))  # 80x80 píxeles

botton_blue_pressed = pygame.image.load("button_blue_pressed.png").convert_alpha()  # Versión "presionada" del botón azul
botton_blue_pressed = pygame.transform.scale(botton_blue_pressed,(80,80))  # 80x80 píxeles

botton_yellow_pressed = pygame.image.load("button_yellow_pressed.png").convert_alpha()  # Versión "presionada" del botón amarillo
botton_yellow_pressed = pygame.transform.scale(botton_yellow_pressed,(80,80))  # 80x80 píxeles

# Estado de los botones (diccionario que guarda si cada tecla está presionada o no)
button_states = {
    'a': False,  # Tecla A (botón rojo): False = no presionada, True = presionada
    's': False,  # Tecla S (botón azul): False = no presionada, True = presionada
    'd': False   # Tecla D (botón amarillo): False = no presionada, True = presionada
}

#--------- VARIABLES DE CONTROL DEL JUEGO ---------
clock = pygame.time.Clock()  # Objeto que controla la velocidad del juego (FPS - frames por segundo)
state = "menu"  # Estado actual del juego: "menu" = pantalla de inicio, "game" = jugando
done = False  # Controla si el juego debe seguir ejecutándose (False = sigue, True = termina)
start_time = None  # Guarda el momento exacto (en milisegundos) cuando empieza el juego, para el temporizador
show_start = True  # Controla si debe mostrar el texto "¡A bailar!" (True = mostrar, False = ocultar)

#--------- FUNCIONES ---------

# PANTALLA DE MENÚ INICIAL
def begin_start():
    screen.blit(background,(0,0))  # Dibuja el fondo del menú en la esquina superior izquierda (posición 0,0)
    small_font = pygame.font.SysFont("Arial",32)  # Crea una fuente Arial de tamaño 32
    message = small_font.render("Presiona ESPACIO para continuar",True,(255,255,255))  # Crea el texto en color blanco
    message_rect = message.get_rect(center=(width/2,height/2+100))  # Calcula la posición centrada (horizontal: 400, vertical: 400)
    screen.blit(message,message_rect)  # Dibuja el texto en la posición calculada

# PANTALLA DEL JUEGO
def start_game():
    global show_start  # Permite modificar la variable global show_start desde dentro de esta función
    screen.blit(background_dance,(0,0))  # Dibuja el fondo del juego (con los 4 carriles)
    
    if show_start:  # Si show_start es True (primeros 3 segundos)...
        font = pygame.font.SysFont("Arial",50)  # Crea fuente Arial tamaño 50
        title = font.render("¡A bailar!",True,(255,255,255))  # Crea el texto "¡A bailar!" en blanco
        title_rect = title.get_rect(center=(width/2,height/2))  # Calcula posición centrada en pantalla
        screen.blit(title,title_rect)  # Dibuja el texto centrado
    else:  # Si show_start es False (después de 3 segundos)...
        draw_game()  # Llama a la función que dibuja los botones y el juego

# ✅ DIBUJA LOS BOTONES DEL JUEGO (esta función SOLO dibuja, NO maneja eventos de teclado)
def draw_game():
    screen.blit(background_dance,(0,0))  # Dibuja primero el fondo del juego
    
    # Botón ROJO (controlado por tecla A) - se posiciona en el carril izquierdo (X=190)
    if button_states['a']:  # Si la tecla A está presionada...
        screen.blit(botton_red_pressed,(190,500))  # Dibuja la versión presionada del botón rojo
    else:  # Si la tecla A NO está presionada...
        screen.blit(botton_red,(190,500))  # Dibuja la versión normal del botón rojo
    
    # Botón AZUL (controlado por tecla S) - se posiciona en el carril del medio (X=300)
    if button_states['s']:  # Si la tecla S está presionada...
        screen.blit(botton_blue_pressed,(300,500))  # Dibuja la versión presionada del botón azul
    else:  # Si la tecla S NO está presionada...
        screen.blit(botton_blue,(300,500))  # Dibuja la versión normal del botón azul
    
    # Botón AMARILLO (controlado por tecla D) - se posiciona en el carril derecho (X=410)
    if button_states['d']:  # Si la tecla D está presionada...
        screen.blit(botton_yellow_pressed,(410,500))  # Dibuja la versión presionada del botón amarillo
    else:  # Si la tecla D NO está presionada...
        screen.blit(botton_yellow,(410,500))  # Dibuja la versión normal del botón amarillo

#--------- LOOP PRINCIPAL DEL JUEGO (se ejecuta 60 veces por segundo) ---------
while not done:  # Mientras done sea False, este loop se repite infinitamente
    
    # ✅ MANEJO DE EVENTOS (clicks, teclas, cerrar ventana, etc)
    for event in pygame.event.get():  # Revisa todos los eventos que ocurrieron en este frame
        if event.type == pygame.QUIT:  # Si el usuario cerró la ventana con la X...
            done = True  # Cambia done a True para salir del loop y terminar el juego
        
        if event.type == pygame.KEYDOWN:  # Si el usuario PRESIONÓ una tecla...
            # Cambio de estado: de menú a juego
            if state == "menu" and event.key == pygame.K_SPACE:  # Si está en el menú Y presionó ESPACIO...
                state = "game"  # Cambia el estado a "game" para empezar a jugar
                start_time = pygame.time.get_ticks()  # Guarda el tiempo actual en milisegundos (ej: 5000 = 5 segundos desde que inició Pygame)
                show_start = True  # Activa la bandera para mostrar "¡A bailar!"
            
            # Volver al menú desde el juego
            if state == "game" and event.key == pygame.K_ESCAPE:  # Si está jugando Y presionó ESC...
                state = "menu"  # Vuelve al menú principal
            
            # ✅ Detecta las teclas del juego A, S, D (solo cuando ya terminó el texto "¡A bailar!")
            if state == "game" and not show_start:  # Si está en estado "game" Y show_start es False...
                if event.key == pygame.K_a:  # Si presionó la tecla A...
                    button_states['a'] = True  # Marca el botón rojo como presionado
                    print("Bailas con A - ROJO")  # Muestra mensaje en consola
                if event.key == pygame.K_s:  # Si presionó la tecla S...
                    button_states['s'] = True  # Marca el botón azul como presionado
                    print("Bailas con S - AZUL")  # Muestra mensaje en consola
                if event.key == pygame.K_d:  # Si presionó la tecla D...
                    button_states['d'] = True  # Marca el botón amarillo como presionado
                    print("Bailas con D - AMARILLO")  # Muestra mensaje en consola
        
        if event.type == pygame.KEYUP:  # Si el usuario SOLTÓ una tecla...
            if event.key == pygame.K_a:  # Si soltó la tecla A...
                button_states['a'] = False  # Marca el botón rojo como NO presionado
                print("Frenas con A")  # Mensaje en consola
            if event.key == pygame.K_s:  # Si soltó la tecla S...
                button_states['s'] = False  # Marca el botón azul como NO presionado
                print("Frenas con S")  # Mensaje en consola
            if event.key == pygame.K_d:  # Si soltó la tecla D...
                button_states['d'] = False  # Marca el botón amarillo como NO presionado
                print("Frenas con D")  # Mensaje en consola
    
    # TEMPORIZADOR: cuenta 3 segundos y luego oculta "¡A bailar!"
    if state == "game" and start_time is not None:  # Si está en modo juego Y el temporizador ya comenzó...
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000  # Calcula cuántos segundos han pasado desde start_time
        # Ejemplo: si start_time=5000 y ahora son 8000 milisegundos → (8000-5000)/1000 = 3 segundos
        if elapsed_time >= 3:  # Si pasaron 3 segundos o más...
            show_start = False  # Oculta el texto "¡A bailar!" y muestra los botones del juego
    
    # DIBUJA LA PANTALLA CORRESPONDIENTE SEGÚN EL ESTADO ACTUAL
    if state == "menu":  # Si el estado es "menu"...
        begin_start()  # Llama a la función que dibuja la pantalla de inicio
    elif state == "game":  # Si el estado es "game"...
        start_game()  # Llama a la función que dibuja la pantalla del juego
    
    pygame.display.flip()  # Actualiza TODA la pantalla (hace visible todo lo que se dibujó en este frame)
    # Sin esta línea, nada de lo que dibujas se vería en la ventana
    
    clock.tick(60)  # Limita el juego a 60 FPS (frames por segundo)
    # Esto significa que el loop while se ejecuta exactamente 60 veces cada segundo
    # Si el código es muy rápido, espera; si es muy lento, intenta alcanzar 60 FPS

pygame.quit()  # Cierra Pygame correctamente cuando termina el loop (done = True)

#Problemas principales