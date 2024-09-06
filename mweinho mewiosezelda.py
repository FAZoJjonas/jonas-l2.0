import matplotlib.pyplot as plt
import numpy as np
import random
import pygame
import sys

# Função para obter mesada
def obter_mesada():
    mesada = []
    for i in range(1, 7):
        while True:
            try:
                valor = float(input(f"Digite o valor da mesada para o mês {i}: R$ "))
                if valor < 0:
                    raise ValueError("O valor não pode ser negativo.")
                mesada.append(valor)
                break
            except ValueError as e:
                print(f"Entrada inválida: {e}. Tente novamente.")
    return mesada

# Função para calcular a média da mesada
def calcular_media(mesada):
    return np.mean(mesada)

# Função para gerar o gráfico da mesada
def gerar_grafico(mesada, media):
    meses = ['Mês 1', 'Mês 2', 'Mês 3', 'Mês 4', 'Mês 5', 'Mês 6']
    
    # Configurações do tema de fogo
    plt.style.use('dark_background')  # Usa um fundo escuro para destacar o tema
    fig, ax = plt.subplots(figsize=(10, 6))

    # Cores inspiradas no fogo
    cor_linha = '#FF4500'  # Laranja avermelhado
    cor_media = '#FFD700'  # Dourado

    # Plotagem da mesada
    ax.plot(meses, mesada, marker='o', linestyle='-', color=cor_linha, label='Mesada Mensal')

    # Adicionando a linha da média
    ax.axhline(y=media, color=cor_media, linestyle='--', label=f'Média: R$ {media:.2f}')

    # Customizações visuais
    ax.set_xlabel('Meses')
    ax.set_ylabel('Valor da Mesada (R$)')
    ax.set_title('Mesada Mensal ao Longo de 6 Meses', fontsize=14, color='orange')
    ax.legend()
    ax.grid(True, linestyle='--', color='gray')
    ax.set_facecolor('#1e1e1e')  # Fundo escuro

    # Personalizando os ticks
    ax.tick_params(axis='both', colors='orange')

    # Exibindo o gráfico
    plt.show()

# Função para jogar o cassino
def jogar_cassino():
    print("\nBem-vindo ao jogo de cassino!")
    print("Você precisa adivinhar um número entre 1 e 10.")
    
    numero_aleatorio = random.randint(1, 10)
    tentativas = 0
    while True:
        try:
            palpite = int(input("Digite seu palpite: "))
            if palpite < 1 or palpite > 10:
                raise ValueError("O palpite deve estar entre 1 e 10.")
            tentativas += 1
            if palpite == numero_aleatorio:
                print(f"\n🔥 Parabéns! Você adivinhou o número em {tentativas} tentativa(s). 🔥")
                break
            elif palpite < numero_aleatorio:
                print("🔥 O número é maior. Tente novamente. 🔥")
            else:
                print("🔥 O número é menor. Tente novamente. 🔥")
        except ValueError as e:
            print(f"🔥 Entrada inválida: {e}. Tente novamente. 🔥")


# Função para jogar o jogo da cobrinha
def jogar_cobrinha():
    pygame.init()
    
    # Configurações da tela
    largura_tela = 600
    altura_tela = 400
    tela = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption("Jogo da Cobrinha")
    
    # Cores
    preto = (0, 0, 0)
    vermelho = (255, 0, 0)  # Vermelho para o tema de fogo
    laranja = (255, 165, 0) # Laranja para o tema de fogo
    amarelo = (255, 255, 0) # Amarelo para o tema de fogo
    
    # Configurações da cobra e comida
    tamanho_cobra = 20
    velocidade = 15
    
    # Função para desenhar a cobra
    def desenhar_cobra(cobra_lista):
        for segmento in cobra_lista:
            pygame.draw.rect(tela, laranja, [segmento[0], segmento[1], tamanho_cobra, tamanho_cobra])
    
    # Função principal do jogo
    def jogo_cobrinha():
        game_over = False
        fechar_jogo = False
        
        x_cobra = largura_tela / 2
        y_cobra = altura_tela / 2
        x_cobra_mudanca = 0
        y_cobra_mudanca = 0
        
        comida_x = round(random.randrange(0, largura_tela - tamanho_cobra) / 20.0) * 20.0
        comida_y = round(random.randrange(0, altura_tela - tamanho_cobra) / 20.0) * 20.0
        
        cobra_lista = []
        comprimento_cobra = 1
        
        while not fechar_jogo:
            while game_over:
                tela.fill(preto)
                fonte = pygame.font.SysFont(None, 35)
                texto = fonte.render("🔥 Game Over! Pressione Q para sair ou C para jogar novamente. 🔥", True, vermelho)
                tela.blit(texto, [largura_tela / 6, altura_tela / 3])
                pygame.display.update()
                
                for evento in pygame.event.get():
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_q:
                            pygame.quit()
                            sys.exit()
                        if evento.key == pygame.K_c:
                            jogo_cobrinha()
            
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT:
                        x_cobra_mudanca = -tamanho_cobra
                        y_cobra_mudanca = 0
                    elif evento.key == pygame.K_RIGHT:
                        x_cobra_mudanca = tamanho_cobra
                        y_cobra_mudanca = 0
                    elif evento.key == pygame.K_UP:
                        y_cobra_mudanca = -tamanho_cobra
                        x_cobra_mudanca = 0
                    elif evento.key == pygame.K_DOWN:
                        y_cobra_mudanca = tamanho_cobra
                        x_cobra_mudanca = 0
            
            if x_cobra >= largura_tela or x_cobra < 0 or y_cobra >= altura_tela or y_cobra < 0:
                game_over = True
            x_cobra += x_cobra_mudanca
            y_cobra += y_cobra_mudanca
            
            tela.fill(preto)
            pygame.draw.rect(tela, amarelo, [comida_x, comida_y, tamanho_cobra, tamanho_cobra])
            cobra_Cabeca = []
            cobra_Cabeca.append(x_cobra)
            cobra_Cabeca.append(y_cobra)
            cobra_lista.append(cobra_Cabeca)
            if len(cobra_lista) > comprimento_cobra:
                del cobra_lista[0]
            
            for segmento in cobra_lista[:-1]:
                if segmento == cobra_Cabeca:
                    game_over = True
            
            desenhar_cobra(cobra_lista)
            pygame.display.update()
            
            if x_cobra == comida_x and y_cobra == comida_y:
                comida_x = round(random.randrange(0, largura_tela - tamanho_cobra) / 20.0) * 20.0
                comida_y = round(random.randrange(0, altura_tela - tamanho_cobra) / 20.0) * 20.0
                comprimento_cobra += 1
            
            pygame.time.Clock().tick(velocidade)
    
    jogo_cobrinha()


# Função principal do menu
def main():
    print("Escolha uma opção:")
    print("1. Calcular a média da mesada e gerar gráfico")
    print("2. Jogar no cassino")
    print("3. Jogar o jogo da cobrinha")
    
    opcao = input("Digite o número da opção escolhida: ")
    
    if opcao == '1':
        mesada = obter_mesada()
        media = calcular_media(mesada)
        print(f"\nA média da mesada durante os 6 meses é: R$ {media:.2f}")
        gerar_grafico(mesada, media)
    elif opcao == '2':
        jogar_cassino()
    elif opcao == '3':
        jogar_cobrinha()
    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

if __name__ == "__main__":
    main()
