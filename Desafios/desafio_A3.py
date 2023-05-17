# Exercício 1
# Calc. de Festa de Jantar
"""
Construir uma calculadora que seja capaz de calcular o
custo de uma festa, que:

Comida custa $25 por pessoa (pp)
Bebida por ser suco, sendo $5 pp com 5%
de desconto na conta, ou Alcoólica,
se $20 pp
E decoração pode ser normal, sendo $30
para mesa e $7.5 de lembranças por
pessoa. Ou Diferenciada, sendo $50 fixo
mais $10 por pessoa.
"""
class CalculadoraFesta:
    def __init__(self):
        self.custo_comida = 25
        self.custo_bebida_saudavel = 5
        self.custo_bebida_alcool = 20
        self.desconto_bebida = 0.05
        self.custo_decoracao_normal_mesa = 30
        self.custo_decoracao_normal_lembrancas = 7.5
        self.custo_decoracao_diferenciada_fixo = 50
        self.custo_decoracao_diferenciada_pessoa = 10

    def calcular_custo_festa(self, num_pessoas, bebida_alcoolica, decoracao_diferenciada):
        custo_total = 0

        # Calcula o custo da comida
        custo_comida = self.custo_comida * num_pessoas
        custo_total += custo_comida

        # Calcula o custo da bebida
        if bebida_alcoolica:
            custo_bebida = self.custo_bebida_alcool * num_pessoas
        else:
            custo_bebida = (self.custo_bebida_saudavel * num_pessoas) * (1 - self.desconto_bebida)
        custo_total += custo_bebida

        # Calcula o custo da decoração
        if decoracao_diferenciada:
            custo_decoracao = self.custo_decoracao_diferenciada_fixo + (self.custo_decoracao_diferenciada_pessoa * num_pessoas)
        else:
            custo_decoracao = self.custo_decoracao_normal_mesa + (self.custo_decoracao_normal_lembrancas * num_pessoas)
        custo_total += custo_decoracao

        return custo_total

calculadora = CalculadoraFesta()
custo_total = calculadora.calcular_custo_festa(50, False, True)
print("O custo total da festa é:", custo_total)


# Exercício 2
# Calc. de Festa de Aniversário
"""
O Buffet agora está expandindo suas atividades e abriu uma nova filial que realiza o
serviço de buffet especializado em festas de aniversários. Além dos serviços oferecidos
pela matriz, comida, bebida e decoração, a filial oferece bolo de aniversário. O bolo é
oferecido em dois tamanhos 8 cm ($40) para festas até 4 pessoas ou 16 cm ($75), para
festas maiores. Esse ainda pode ser personalizado, ao custo de $0.25 por caractere, com
um mensagem de escolha do cliente (o bolo de 8 cm comporta um texto de até 16
caracteres enquanto o de 16 cm, até 40).
"""
class CalculadoraFesta:
    def __init__(self):
        self.custo_comida = 25
        self.custo_bebida_saudavel = 5
        self.custo_bebida_alcool = 20
        self.desconto_bebida = 0.05
        self.custo_decoracao_normal_mesa = 30
        self.custo_decoracao_normal_lembrancas = 7.5
        self.custo_decoracao_diferenciada_fixo = 50
        self.custo_decoracao_diferenciada_pessoa = 10
        self.custo_bolo_8cm = 40
        self.custo_bolo_16cm = 75
        self.custo_personalizacao_caractere = 0.25
        self.limite_caracteres_bolo_8cm = 16
        self.limite_caracteres_bolo_16cm = 40

    def calcular_custo_festa(self, num_pessoas, bebida_alcoolica, decoracao_diferenciada, tamanho_bolo=None, mensagem_bolo=""):
        custo_total = 0

        # Calcula o custo da comida
        custo_comida = self.custo_comida * num_pessoas
        custo_total += custo_comida

        # Calcula o custo da bebida
        if bebida_alcoolica:
            custo_bebida = self.custo_bebida_alcool * num_pessoas
        else:
            custo_bebida = (self.custo_bebida_saudavel * num_pessoas) * (1 - self.desconto_bebida)
        custo_total += custo_bebida

        # Calcula o custo da decoração
        if decoracao_diferenciada:
            custo_decoracao = self.custo_decoracao_diferenciada_fixo + (self.custo_decoracao_diferenciada_pessoa * num_pessoas)
        else:
            custo_decoracao = self.custo_decoracao_normal_mesa + (self.custo_decoracao_normal_lembrancas * num_pessoas)
        custo_total += custo_decoracao

        # Calcula o custo do bolo e personalização, se selecionado
        if tamanho_bolo == "8cm":
            custo_bolo = self.custo_bolo_8cm
            limite_caracteres = self.limite_caracteres_bolo_8cm
        elif tamanho_bolo == "16cm":
            custo_bolo = self.custo_bolo_16cm
            limite_caracteres = self.limite_caracteres_bolo_16cm
        else:
            custo_bolo = 0
            limite_caracteres = 0

        if mensagem_bolo:
            caracteres_excedidos = max(len(mensagem_bolo) - limite_caracteres, 0)
            custo_personalizacao = caracteres_excedidos * self.custo_personalizacao_caractere
            custo_bolo += custo_personalizacao

        custo_total += custo_bolo

        return custo_total

# Criando uma instância da CalculadoraFesta
calculadora = CalculadoraFesta()

# Exemplo 1: Festa de aniversário com bolo de 8cm e sem personalização
num_pessoas = 10
bebida_alcoolica = False
decoracao_diferenciada = False
tamanho_bolo = "8cm"
mensagem_bolo = ""

custo_total = calculadora.calcular_custo_festa(num_pessoas, bebida_alcoolica, decoracao_diferenciada, tamanho_bolo, mensagem_bolo)
print("Custo total da festa:", custo_total)

# Exemplo 2: Festa de aniversário com bolo de 16cm e personalização
num_pessoas = 20
bebida_alcoolica = True
decoracao_diferenciada = True
tamanho_bolo = "16cm"
mensagem_bolo = "Feliz Aniversário!"

custo_total = calculadora.calcular_custo_festa(num_pessoas, bebida_alcoolica, decoracao_diferenciada, tamanho_bolo, mensagem_bolo)
print("Custo total da festa:", custo_total)