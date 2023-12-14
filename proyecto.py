import pygame
import sys

pygame.init()

# Definición de colores
black = (0, 0, 0)
white = (255, 255, 255)
screen_size = (800, 600)
player_width = 15
player_height = 90

screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Coordenadas y velocidad Player 1
player1_x_coor = 50
player1_y_coor = 300 - player_height // 2
player1_y_speed = 0

# Coordenadas y velocidad Player 2
player2_x_coor = 750 - player_width
player2_y_coor = 300 - player_height // 2
player2_y_speed = 0

# Coordenadas pong
pelota_x = 400
pelota_y = 300
pelota_speed_x = 3
pelota_speed_y = 3

game_over = False

def show_menu():
    text = font.render("¡La pelota salió! ¿Qué quieres hacer?", True, white)
    screen.blit(text, (200, 200))

    text_restart = font.render("1. Iniciar nuevamente", True, white)
    screen.blit(text_restart, (250, 250))

    text_exit = font.render("2. Salir del juego", True, white)
    screen.blit(text_exit, (250, 300))

def handle_key_events():
    keys = pygame.key.get_pressed()

    # Interacción Player 1
    player1_y_speed = (keys[pygame.K_s] - keys[pygame.K_w]) * 3

    # Interacción Player 2
    player2_y_speed = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 3

    return player1_y_speed, player2_y_speed

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    player1_y_speed, player2_y_speed = handle_key_events()

    # Limitar movimiento de Player 1 dentro de los límites de la pantalla
    player1_y_coor = max(0, min(player1_y_coor + player1_y_speed, screen_size[1] - player_height))

    # Limitar movimiento de Player 2 dentro de los límites de la pantalla
    player2_y_coor = max(0, min(player2_y_coor + player2_y_speed, screen_size[1] - player_height))

    if pelota_y > 590 or pelota_y < 10:
        pelota_speed_y *= -1

    # Salida de la pelota / Derecho e Izquierdo
    if pelota_x > 800 or pelota_x < 0:
        show_menu()
        pygame.display.flip()

        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        pelota_x, pelota_y = 400, 300
                        pelota_speed_x = 3
                        pelota_speed_y = 3
                        waiting_for_input = False
                    elif event.key == pygame.K_2:
                        game_over = True
                        waiting_for_input = False

    # Movimiento pelota
    pelota_x += pelota_speed_x
    pelota_y += pelota_speed_y

    screen.fill(black)

    # ------Zona de dibujo
    jugador1 = pygame.draw.rect(screen, white, (player1_x_coor, player1_y_coor, player_width, player_height))
    jugador2 = pygame.draw.rect(screen, white, (player2_x_coor, player2_y_coor, player_width, player_height))
    pelota = pygame.draw.circle(screen, white, (pelota_x, pelota_y), 10)
    # ------Zona de dibujo

    # Coliciones
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        pelota_speed_x *= -1

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
