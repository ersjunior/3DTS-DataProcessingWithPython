"""
1) Escreva um programa que lê do teclado e registra em uma matriz (3x6), 
a receita de 3 (três) empresas do último semestre (6 meses). 
Após ler a receita de cada empresa mes a mes, seu programa deve então retornar a 
Média e o Desvio Padrão Populacional das receitas do semestre 
para cada uma das empresas.
"""
import numpy as np

# Inicializar a matriz de receitas
receitas = np.zeros((3, 6))

# Ler as receitas de cada empresa mês a mês
for i in range(3):
    print("Empresa", i+1)
    for j in range(6):
        receitas[i, j] = float(input("Digite a receita do mês {}: ".format(j+1)))

# Calcular a média e o desvio padrão populacional das receitas do semestre para cada empresa
medias = np.mean(receitas, axis=1)
desvios_padrao = np.std(receitas, axis=1, ddof=0)

# Imprimir os resultados
for i in range(3):
    print("Empresa", i+1)
    print("Média:", medias[i])
    print("Desvio padrão populacional:", desvios_padrao[i])
    print()

"""
2) Crie um programa no qual você deve ler do teclado todas as compras de 6 (seis) ações/ativos 
realizadas em um dia, coletando informações de preço e quantidade para cada uma. 
Armazene essa informação em uma matriz 1x6 com os preços. 
Já as quantidades armazenadas em uma outra matriz 6x1. De posse dessas duas informações 
realize o cálculo final do montante em dinheiro de ativos adquiridos neste dia para sua carteira.
"""
import numpy as np

# Ler os preços das ações
precos = np.zeros((1, 6))
for i in range(6):
    precos[0, i] = float(input("Digite o preço da ação {}: ".format(i+1)))

# Ler as quantidades das ações
quantidades = np.zeros((6, 1))
for i in range(6):
    quantidades[i, 0] = float(input("Digite a quantidade da ação {}: ".format(i+1)))

# Calcular o montante em dinheiro de ativos adquiridos
montante = np.dot(precos, quantidades)

# Imprimir o resultado
print("Montante em dinheiro de ativos adquiridos: R$", montante[0, 0])


"""
3) Uma corretora que trabalha com 3 ativos principais VALE5, PETR4 e BBDC4, 
gostaria de registrar os rendimentos da semana em uma matriz 5x3. 
Crie um programa que lê do teclado dia-a-dia o rendimento de cada um dos 3 ativos. 
Em seguida o programa deve fazer o cálculo de rendimento acumulado de cada ativo na semana. 
E por fim, apresenta o rendimento médio total do fundo.
"""
import numpy as np

# Inicializar a matriz de rendimentos
rendimentos = np.zeros((5, 3))

# Ler os rendimentos de cada ativo dia-a-dia
for i in range(5):
    print("Dia", i+1)
    for j in range(3):
        rendimentos[i, j] = float(input("Digite o rendimento do ativo {}: ".format(j+1)))

# Calcular o rendimento acumulado de cada ativo na semana
rendimentos_acumulados = np.cumprod(1 + rendimentos, axis=0) - 1

# Calcular o rendimento médio total do fundo
rendimento_medio = np.mean(rendimentos)

# Imprimir os resultados
for j in range(3):
    print("Ativo", j+1)
    print("Rendimento acumulado na semana:", rendimentos_acumulados[-1, j])
    print()
print("Rendimento médio total do fundo:", rendimento_medio)


"""
4) As 3 principais cidades brasileiras estão preocupadas com a taxa de ocupação de hospitais durante o COVID. 
Crie um programa que lê do teclado dia a dia para cada cidade e registra em uma matriz 7x3 a 
taxa de ocupação dos hospitais dessas 3 cidades nos última semana (7 dias). 
Seu programa deve apresentar então o mínimo, máximo e média de ocupação dos leitos para cada cidade.
"""
import numpy as np

# Inicializar a matriz de taxa de ocupação dos leitos
taxas_ocupacao = np.zeros((7, 3))

# Ler as taxas de ocupação dos leitos dia a dia para cada cidade
for i in range(7):
    print("Dia", i+1)
    for j in range(3):
        taxas_ocupacao[i, j] = float(input("Digite a taxa de ocupação da cidade {}: ".format(j+1)))

# Calcular o mínimo, máximo e média de ocupação dos leitos para cada cidade
minimos = np.min(taxas_ocupacao, axis=0)
maximos = np.max(taxas_ocupacao, axis=0)
medias = np.mean(taxas_ocupacao, axis=0)

# Imprimir os resultados
for j in range(3):
    print("Cidade", j+1)
    print("Mínimo de ocupação:", minimos[j])
    print("Máximo de ocupação:", maximos[j])
    print("Média de ocupação:", medias[j])
    print()
