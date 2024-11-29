import pygame
import time
import random

# Inicialização do Pygame
pygame.init()

# Cores
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Dimensões da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Configurações da tela cheia
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption('Jogo da Cobrinha')

# Carregar imagens
snake_img = pygame.image.load('cobra.png')
food_img = pygame.image.load('bife.png')
background_img = pygame.image.load('fundo.png')  # Carregue sua imagem de fundo aqui

# Redimensionar imagens
BLOCK_SIZE = 50
snake_img = pygame.transform.scale(snake_img, (BLOCK_SIZE, BLOCK_SIZE))
food_img = pygame.transform.scale(food_img, (BLOCK_SIZE, BLOCK_SIZE))
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Função para desenhar a cobrinha
def draw_snake(snake_list):
    for x in snake_list:
        screen.blit(snake_img, (x[0], x[1]))

# Função para o menu
def menu():
    while True:
        screen.fill(GREEN)
        font_style = pygame.font.SysFont("bahnschrift", 50)
        
        title = font_style.render("Jogo da Cobrinha", True, WHITE)
        start_button = font_style.render("Começar", True, WHITE)
        exit_button = font_style.render("Sair", True, WHITE)

        # Centraliza o texto
        title_rect = title.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
        start_rect = start_button.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        exit_rect = exit_button.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.5))

        screen.blit(title, title_rect)
        screen.blit(start_button, start_rect)
        screen.blit(exit_button, exit_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if start_rect.collidepoint(mouse_x, mouse_y):
                    game_loop()
                if exit_rect.collidepoint(mouse_x, mouse_y):
                    pygame.quit()
                    quit()

# Função para o jogo
def game_loop():
    game_over = False
    game_close = False

    x1 = SCREEN_WIDTH / 2
    y1 = SCREEN_HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            font_style = pygame.font.SysFont("bahnschrift", 50)
            mesg = font_style.render("Você perdeu! Pressione C para jogar novamente ou Q para sair.", True, WHITE)
            screen.blit(mesg, [SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = BLOCK_SIZE
                    x1_change = 0

        if x1 >= SCREEN_WIDTH or x1 < 0 or y1 >= SCREEN_HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        
        # Desenhar fundo
        screen.blit(background_img, (0, 0))

        # Desenhar comida
        screen.blit(food_img, (food_x, food_y))

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(snake_list)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            food_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            snake_length += 1

        time.sleep(0.1)

    pygame.quit()

# Executar o menu
menu()
