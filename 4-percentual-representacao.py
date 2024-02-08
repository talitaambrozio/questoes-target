"""
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP - R$67.836,43
RJ - R$36.678,66
MG - R$29.229,88
ES - R$27.165,48
Outros - R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação
que cada estado teve dentro do valor total mensal da distribuidora.


"""
faturamento_mensal = [('SP', 67836.43), ('RJ', 36678.66), ('MG', 29229.88), ('ES', 27165.48), ('Outros', 19849.53)]
total_faturamento = 0
for f in faturamento_mensal:
    total_faturamento += f[1]

print(f'Total de faturamento mensal: R${total_faturamento}')

for f in faturamento_mensal:
    perc_participacao = f[1]/total_faturamento*100
    print(f'% participação {f[0]}: {perc_participacao:.2f}')