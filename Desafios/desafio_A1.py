'''
Exercício 1
1) Calcule a nota final, dado que AP1 e AP2 tem peso 40% e AP3 20%
'''
def calcular_nota_final(ap1, ap2, ap3):
    nota_final = ap1 * 0.4 + ap2 * 0.4 + ap3 * 0.2
    return nota_final

a1=float(input("Digite a nota da AP1: "))
a2=float(input("Digite a nota da AP2: "))
a3=float(input("Digite a nota da AP3: "))
nota_final = calcular_nota_final(a1, a2, a3)
print(f"Nota final: {nota_final}")




'''
Exercício 2
2) Calcule a nota como conceito, com sendo A (maior que 9), B (entre 7 e 9), D (entre 5 e 7), F (abaixo disto)
'''
def calcular_nota_conceito(nota): 
  if nota >= 9: 
    return "A" 
  elif nota < 9 and nota >= 7: 
    return "B" 
  elif nota < 7 and nota >= 5: 
    return "D" 
  else: 
    return "F" 
    
nota = calcular_nota_conceito(float(input("Informe sua nota: "))) 
print(nota)




'''
Exercício 3
3) Calcular o imposto de renda devido com base no salário mensal e regra da Receita Federal
'''
salario = float(input('Qual o salário? '))
def irrf(salario):
  if salario >= 3743.19:
    return(f'O salário é {salario}, a alíquota é {round((salario * 27.5 / 100),2)} e a dedução é {round((salario * 27.5 / 100) - 692.78,2)}')
  elif salario < 3743.19 or salario >= 2995.71:
    return(f'O salário é {salario}, a alíquota é {round((salario * 22.5 / 100),2)} e a dedução é {round((salario * 27.5 / 100)- 505.62,2)}')
  elif salario < 2995.71 or salario >= 2246.76:
    return(f'O salário é {salario}, a alíquota é {round((salario * 15.0 / 100),2)} e a dedução é {round((salario * 27.5 / 100) - 280.94,2)}')
  elif salario < 2246.76 or salario >= 1499.16:
    return(f'O salário é {salario}, a alíquota é {round((salario * 7.5 / 100),2)} e a dedução é {round((salario * 27.5 / 100) - 112.43,2)}')
  else:
    return(f'O salário é {salario} e está isento dedução')

irrf(salario)




'''
Uma loja apresenta um cartaz de um produto indicando o valor a vista, em comparação ao valor parcelado em 2 vezes (para 30 e 60 dias), mas não cumpre a resolução do Banco Central de apresentar a taxa de juros embutida bcb.gov.br/pre/normativos/busca/downloadNormativo.asp?arquivo=/L ists/Normativos/Attachments/48005/Res_3517_v1_O.pdf Crie uma função que dado valor a vista, o valor das parcelas, calcule o juros deste financiamento Atenção: Existem ao menos duas formas de resolução, uma de maneira algébrica, ou seja, desenvolva a equação. E outra de maneira por aproximação, seu programa vai testando soluções (não aleatórias) que vai se aproximando do resultado correto. Para esta opção, até 0.3% de erro no seu cálculo é aceito. Desafio: Utilizando o método de aproximação como solução, estenda seu programa para ao invés de trabalhar com apenas 2 parcelas, trabalhe com N.
'''
def calcular_taxa_juros(valor_vista, valor_parcelas, n_parcelas):
    margem_erro = 0.003
    taxa_juros = 0.01
    taxa_maxima = 100.0

    while True:
        valor_total = valor_parcelas * (((1 + taxa_juros)**n_parcelas - 1) / (taxa_juros * (1 + taxa_juros)**n_parcelas))
        
        diferenca = valor_total - valor_vista
        
        if abs(diferenca / valor_vista) <= margem_erro:
            return taxa_juros * 100
        
        taxa_juros = taxa_juros * (1 + diferenca / valor_vista)
        if taxa_juros > taxa_maxima:
            raise ValueError("Não foi possível encontrar uma taxa de juros dentro da margem de erro permitida.")

# Usando a função
valor_vista = 100.0
parcelas = 60.0
n = 2
taxa_juros = calcular_taxa_juros(valor_vista, parcelas, n)
print(f"Taxa de juros: {taxa_juros:.2f}%")
