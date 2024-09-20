import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Minerador")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Preços dos minérios
COAL_VALUE = 50
IRON_VALUE = 200
DIAMOND_VALUE = 500

# Estado do jogo
money = 0
mined_resources = {'carvão': 0, 'ferro': 0, 'diamante': 0}
current_resource = 'carvão'  # Começa minerando carvão

# Carrega as imagens dos minérios
coal_image = pygame.image.load('carvao.png')
iron_image = pygame.image.load('ferro.jpg')
diamond_image = pygame.image.load('diamante.png')

# Função para desenhar a tela
def draw_screen():
    screen.fill(WHITE)
    
    # Centraliza o minério atual na tela
    if current_resource == 'carvão':
        current_image = coal_image
    elif current_resource == 'ferro':
        current_image = iron_image
    elif current_resource == 'diamante':
        current_image = diamond_image

    # Calcula a posição centralizada
    x_position = screen_width // 2 - current_image.get_width() // 2
    y_position = screen_height // 2 - current_image.get_height() // 2

    # Desenha o contador de dinheiro acima do minério
    font = pygame.font.SysFont(None, 36)
    money_text = font.render(f"Dinheiro: ${money}", True, BLACK)
    screen.blit(money_text, (x_position, y_position - 40))  # Posição acima do minério

    # Desenha o minério atual
    screen.blit(current_image, (x_position, y_position))

    # Desenha o status de mineração
    resource_text = font.render(f"Minerando: {current_resource}", True, BLACK)
    screen.blit(resource_text, (20, 20))

    pygame.display.flip()

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                # Muda o recurso atual
                if current_resource == 'carvão':
                    current_resource = 'ferro'
                elif current_resource == 'ferro':
                    current_resource = 'diamante'
                else:
                    current_resource = 'carvão'
                    
            if event.key == pygame.K_m:
                # Minerar o recurso atual
                if current_resource == 'carvão':
                    money += COAL_VALUE
                    mined_resources['carvão'] += 1
                elif current_resource == 'ferro':
                    money += IRON_VALUE
                    mined_resources['ferro'] += 1
                elif current_resource == 'diamante':
                    money += DIAMOND_VALUE
                    mined_resources['diamante'] += 1

    draw_screen()
