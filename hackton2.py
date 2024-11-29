import pygame
import random
import time
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Importar o Pillow para carregar a imagem

# ============================== Jogo Intergalactic ==============================

# Inicializando o Pygame
pygame.init()

# Definir dimensões da tela para tela cheia
largura_tela = pygame.display.Info().current_w  # Largura da tela inteira
altura_tela = pygame.display.Info().current_h  # Altura da tela inteira
tela = pygame.display.set_mode((largura_tela, altura_tela), pygame.FULLSCREEN)
pygame.display.set_caption('Jogo Intergalactic')

# Definir cores
preto = (0, 0, 0)
branco = (255, 255, 255)
azul = (0, 0, 255)
vermelho = (255, 0, 0)

# Definir tamanhos
tamanho_nave = 50  # Tamanho da nave
tamanho_projétil = 10  # Tamanho do projétil
velocidade_nave = 5  # Velocidade da nave
velocidade_projétil = 7  # Velocidade do projétil
velocidade_inimigo = 3  # Velocidade dos inimigos

# Função para carregar e redimensionar imagens
def carregar_imagem(caminho, tamanho):
    imagem = Image.open(caminho)
    imagem = imagem.resize(tamanho, Image.Resampling.LANCZOS)  # Redimensiona a imagem usando LANCZOS
    return pygame.image.fromstring(imagem.tobytes(), imagem.size, imagem.mode)

# Reduzir o tamanho das imagens para a metade
metade_tamanho_nave = (tamanho_nave // 1, tamanho_nave // 1)
metade_tamanho_projétil = (tamanho_projétil, 20)  # Projétil mantém o tamanho original
metade_tamanho_inimigo = (tamanho_nave // 1, tamanho_nave // 1)

# Carregar imagens e redimensionar
nave_imagem = carregar_imagem('nave.png', metade_tamanho_nave)  # Substitua com o caminho da sua imagem de nave
inimigo_imagem = carregar_imagem('inimigo.png', metade_tamanho_inimigo)  # Substitua com o caminho da sua imagem de inimigo
projétil_imagem = pygame.Surface(metade_tamanho_projétil)
projétil_imagem.fill(azul)

# Função para desenhar a nave
def desenhar_nave(x, y):
    tela.blit(nave_imagem, (x, y))

# Função para desenhar os projéteis
def desenhar_projétil(projétils):
    for projétil in projétils:
        pygame.draw.rect(tela, azul, (projétil[0], projétil[1], tamanho_projétil, 20))

# Função para desenhar os inimigos
def desenhar_inimigos(inimigos):
    for inimigo in inimigos:
        tela.blit(inimigo_imagem, (inimigo[0], inimigo[1]))

# Função para movimentar os inimigos
def mover_inimigos(inimigos):
    for inimigo in inimigos:
        inimigo[1] += velocidade_inimigo
        if inimigo[1] > altura_tela:
            inimigo[1] = random.randint(-50, -10)
            inimigo[0] = random.randint(0, largura_tela - tamanho_nave)

# Função principal do jogo
def jogo_intergalactic():
    # Posições iniciais
    x_nave = largura_tela // 2 - metade_tamanho_nave[0] // 2
    y_nave = altura_tela - metade_tamanho_nave[1] - 10
    x_mudar = 0

    # Projéteis e inimigos
    projétils = []
    inimigos = []

    clock = pygame.time.Clock()
    game_over = False
    inimigos_timer = time.time()

    while not game_over:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x_mudar = -velocidade_nave
                elif evento.key == pygame.K_RIGHT:
                    x_mudar = velocidade_nave
                elif evento.key == pygame.K_SPACE:
                    # Dispara um projétil
                    projétils.append([x_nave + metade_tamanho_nave[0] - tamanho_projétil // 2, y_nave])

            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                    x_mudar = 0

        # Movimentar a nave
        x_nave += x_mudar
        if x_nave < 0:
            x_nave = 0
        elif x_nave > largura_tela - metade_tamanho_nave[0]:
            x_nave = largura_tela - metade_tamanho_nave[0]

        # Atualizar projéteis
        for projétil in projétils[:]:
            projétil[1] -= velocidade_projétil
            if projétil[1] < 0:
                projétils.remove(projétil)

        # Adicionar inimigos a cada 10 segundos
        if time.time() - inimigos_timer > 10:
            inimigos_timer = time.time()
            inimigos.append([random.randint(0, largura_tela - metade_tamanho_inimigo[0]), -metade_tamanho_inimigo[1]])

        # Mover os inimigos
        mover_inimigos(inimigos)

        # Verificar colisões (projétil com inimigos)
        for projétil in projétils[:]:
            for inimigo in inimigos[:]:
                if projétil[0] < inimigo[0] + metade_tamanho_inimigo[0] and projétil[0] + tamanho_projétil > inimigo[0] and \
                        projétil[1] < inimigo[1] + metade_tamanho_inimigo[1] and projétil[1] + 20 > inimigo[1]:
                    projétils.remove(projétil)
                    inimigos.remove(inimigo)

        # Preencher o fundo e desenhar elementos
        tela.fill(preto)
        desenhar_nave(x_nave, y_nave)
        desenhar_projétil(projétils)
        desenhar_inimigos(inimigos)

        pygame.display.update()

        # Controlar FPS
        clock.tick(60)

    pygame.quit()
    quit()

# ========================== Interface Gráfica =======================

class InterfaceGrafica:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema Integrado")

        # Inicializar o saldo da conta bancária
        self.saldo = 1000  # Saldo inicial

        # Carregar e configurar o fundo PNG
        self.background_image = Image.open("tijolo.jpg")  # Substitua pelo caminho da sua imagem de fundo
        self.background_image = self.background_image.resize((largura_tela, altura_tela))  # Redimensiona para preencher toda a tela
        self.bg_photo = ImageTk.PhotoImage(self.background_image)
        
        # Criar um label para exibir a imagem de fundo
        self.bg_label = tk.Label(self.master, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)  # Ajusta o fundo para preencher toda a janela

        # Criar os botões
        self.botao_banco = tk.Button(self.master, text="Banco", width=20, height=2, command=self.abrir_banco)
        self.botao_banco.pack(pady=10)

        self.botao_juros = tk.Button(self.master, text="Calculadora de Juros Compostos", width=30, height=2, command=self.abrir_juros)
        self.botao_juros.pack(pady=10)

        self.botao_jogo = tk.Button(self.master, text="Jogo Intergalactic", width=20, height=2, command=self.abrir_jogo)
        self.botao_jogo.pack(pady=10)

    def abrir_banco(self):
        banco_window = tk.Toplevel(self.master)
        banco_window.title("Banco")
        banco_window.geometry("400x300")

        # Exibir saldo
        self.saldo_label = tk.Label(banco_window, text=f"Saldo: R$ {self.saldo:.2f}", font=("Arial", 16))
        self.saldo_label.pack(pady=10)

        # Entrada para depósito
        self.deposito_label = tk.Label(banco_window, text="Valor para depósito:")
        self.deposito_label.pack(pady=5)
        self.deposito_entry = tk.Entry(banco_window)
        self.deposito_entry.pack(pady=5)

        # Botão de depósito
        self.deposito_button = tk.Button(banco_window, text="Depositar", command=self.depositar)
        self.deposito_button.pack(pady=10)

        # Entrada para saque
        self.saque_label = tk.Label(banco_window, text="Valor para saque:")
        self.saque_label.pack(pady=5)
        self.saque_entry = tk.Entry(banco_window)
        self.saque_entry.pack(pady=5)

        # Botão de saque
        self.saque_button = tk.Button(banco_window, text="Sacar", command=self.sacar)
        self.saque_button.pack(pady=10)

        # Botão para consultar saldo
        self.consultar_button = tk.Button(banco_window, text="Consultar Saldo", command=self.consultar_saldo)
        self.consultar_button.pack(pady=10)

    def depositar(self):
        try:
            valor = float(self.deposito_entry.get())
            if valor > 0:
                self.saldo += valor
                messagebox.showinfo("Depósito", f"Depósito de R$ {valor:.2f} realizado com sucesso!")
                self.saldo_label.config(text=f"Saldo: R$ {self.saldo:.2f}")
            else:
                messagebox.showerror("Erro", "O valor do depósito deve ser positivo.")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um valor válido.")

    def sacar(self):
        try:
            valor = float(self.saque_entry.get())
            if valor > 0:
                if valor <= self.saldo:
                    self.saldo -= valor
                    messagebox.showinfo("Saque", f"Saque de R$ {valor:.2f} realizado com sucesso!")
                    self.saldo_label.config(text=f"Saldo: R$ {self.saldo:.2f}")
                else:
                    messagebox.showerror("Erro", "Saldo insuficiente para o saque.")
            else:
                messagebox.showerror("Erro", "O valor do saque deve ser positivo.")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um valor válido.")

    def consultar_saldo(self):
        messagebox.showinfo("Consulta de Saldo", f"Seu saldo atual é: R$ {self.saldo:.2f}")

    def abrir_juros(self):
        # Janela para a calculadora de Juros Compostos
        juros_window = tk.Toplevel(self.master)
        juros_window.title("Calculadora de Juros Compostos")
        juros_window.geometry("400x300")

        # Labels e campos de entrada
        self.investimento_label = tk.Label(juros_window, text="Valor Investido (R$):")
        self.investimento_label.pack(pady=5)
        self.investimento_entry = tk.Entry(juros_window)
        self.investimento_entry.pack(pady=5)

        self.taxa_label = tk.Label(juros_window, text="Taxa de Juros Anual (%):")
        self.taxa_label.pack(pady=5)
        self.taxa_entry = tk.Entry(juros_window)
        self.taxa_entry.pack(pady=5)

        self.anos_label = tk.Label(juros_window, text="Quantidade de Anos:")
        self.anos_label.pack(pady=5)
        self.anos_entry = tk.Entry(juros_window)
        self.anos_entry.pack(pady=5)

        self.calcular_button = tk.Button(juros_window, text="Calcular", command=self.calcular_juros)
        self.calcular_button.pack(pady=10)

        # Label para exibir o resultado
        self.resultado_label = tk.Label(juros_window, text="Valor Futuro: R$ 0.00", font=("Arial", 14))
        self.resultado_label.pack(pady=10)

    def calcular_juros(self):
        try:
            P = float(self.investimento_entry.get())  # Valor investido
            r = float(self.taxa_entry.get())  # Taxa de juros anual
            t = int(self.anos_entry.get())  # Quantidade de anos

            if P > 0 and r > 0 and t > 0:
                A = P * (1 + r / 100) ** t
                self.resultado_label.config(text=f"Valor Futuro: R$ {A:.2f}")
            else:
                messagebox.showerror("Erro", "Por favor, insira valores válidos.")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

    def abrir_jogo(self):
        self.master.withdraw()  # Fecha a janela do Tkinter
        jogo_intergalactic()

# ========================= Rodando a interface =========================

if __name__ == "__main__":
    root = tk.Tk()
    interface = InterfaceGrafica(root)
    root.mainloop()
