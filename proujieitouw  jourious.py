import matplotlib.pyplot as plt  # Importa a biblioteca matplotlib.pyplot para criar gráficos.

def calcular_montante(valor_inicial, taxa_juros, anos):
    # Função que calcula o montante final de um investimento.
    return valor_inicial * (1 + taxa_juros) ** anos

# Solicita ao usuário o valor inicial do investimento e converte para float.
valor_inicial = float(input('Informe o valor inicial do investimento: '))

# Solicita a taxa de juros em porcentagem, converte para decimal (por exemplo, 5% se torna 0.05).
taxa_juros = float(input('Informe a taxa de juros em (%): ')) / 100

# Solicita a quantidade de anos de investimento e converte para inteiro.
anos = int(input('Informe a quantidade de anos de investimento: '))

# Cria uma lista vazia para armazenar os montantes ao longo dos anos.
montantes = []

# Loop que itera de 1 até o número de anos especificado pelo usuário.
for ano in range(1, anos + 1):
    # Calcula o montante para o ano atual usando a função calcular_montante.
    montante = calcular_montante(valor_inicial, taxa_juros, ano)
    
    # Adiciona o montante calculado à lista montantes.
    montantes.append(montante)

# O montante final após todos os anos é o último valor da lista montantes.
montante_final = montantes[-1]

# Imprime o montante final formatado com duas casas decimais.
print(f'O montante final após {anos} anos será de R$: {montante_final:.2f}')

# Cria uma lista de anos para o eixo X do gráfico.
anos_lista = list(range(1, anos + 1))

# Plota os dados no gráfico com os anos no eixo X e os montantes no eixo Y.
plt.plot(anos_lista, montantes, marker='o')

# Define o título do gráfico.
plt.title('Crescimento do Investimento ao Longo dos Anos')

# Define o rótulo do eixo X.
plt.xlabel('Anos de Investimento')

# Define o rótulo do eixo Y.
plt.ylabel('Montante (R$)')

# Exibe o gráfico na tela.
plt.show()
