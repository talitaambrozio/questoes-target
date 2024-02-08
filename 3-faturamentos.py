"""
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, 
faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias 
devem ser ignorados no cálculo da média;
"""
import json


class Faturamento:
    def __init__(self, dia, valor):
        self.dia = dia
        self.valor = valor

lista_faturamentos = []
try:
    with open('dados.json', 'r') as arquivo:
        faturamentos = json.load(arquivo)
        for faturamento in faturamentos:
            fat = Faturamento(**faturamento)
            lista_faturamentos.append(fat)            
        print('Dados do arquivo JSON inseridos com sucesso.')
        
except FileNotFoundError:
        print('Arquivo não encontrado.')
except json.JSONDecodeError:
        print('Erro ao decodificar o arquivo JSON.')
        
#Impressão da lista completa de faturamento:        
for f in lista_faturamentos:
    print(f'dia: {f.dia} valor: R${f.valor:.2f}')


#Encontrando o menor e maior valor de faturamento ocorrido em um dia do mês:
valores_faturamentos = [f.valor for f in lista_faturamentos]
valores_faturamentos_nao_zerados = [f.valor for f in lista_faturamentos if f.valor > 0 ]
menor_faturamento = min(valores_faturamentos_nao_zerados)
maior_faturamento = max(valores_faturamentos)

qtd_dias_fat_superior_media = 0
soma_faturamento = 0
qtd_dias_com_faturamento = 0

#Encontrando a média mensal de faturamento
for f in lista_faturamentos:
    if f.valor > 0:
        soma_faturamento += f.valor
        qtd_dias_com_faturamento += 1
        
media_mensal_faturamento = soma_faturamento/qtd_dias_com_faturamento

#Encontrando a quantidade de dias que o faturamento superou à média mensal:
for f in lista_faturamentos:
    if f.valor > media_mensal_faturamento:
        qtd_dias_fat_superior_media += 1
        
print(f'Faturamento total do mês: R${sum(valores_faturamentos):.2f}')        
print(f'O menor valor de faturamento foi de: R${menor_faturamento:.2f}')
print(f'O maior valor de faturamento foi de: R${maior_faturamento:.2f}')
print(f'A média mensal de faturamento é de R${media_mensal_faturamento:.2f}')        
print(f'O número de dias no mês em que o valor de faturamento diário superou à media mensal é de {qtd_dias_fat_superior_media} dias')        


