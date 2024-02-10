import json


def calcular_min_max_faturamento(faturamento_diario):
    if faturamento_diario:
        menor = min(faturamento_diario)
        maior = max(faturamento_diario)
    else:
        menor = None
        maior = None
    return menor, maior


def calcular_dias_acima_media(faturamento_diario, media_mensal):
    dias_acima_media = sum(1 for faturamento in faturamento_diario if faturamento > media_mensal)
    return dias_acima_media
with open('dados.json') as arquivo_json:
    dados_faturamento = json.load(arquivo_json)

faturamento_diario = [dia['valor'] for dia in dados_faturamento]


faturamento_diario_sem_zero = [faturamento for faturamento in faturamento_diario if faturamento != 0]


menor_faturamento, maior_faturamento = calcular_min_max_faturamento(faturamento_diario_sem_zero)


if faturamento_diario_sem_zero:
   
    media_mensal = sum(faturamento_diario_sem_zero) / len(faturamento_diario_sem_zero)
else:
    
    media_mensal = 0
    print("Não houve faturamento durante o mês.")

dias_acima_media = calcular_dias_acima_media(faturamento_diario_sem_zero, media_mensal)

print(f"Menor valor de faturamento diário: {menor_faturamento}")
print(f"Maior valor de faturamento diário: {maior_faturamento}")
print(f"Número de dias com faturamento diário acima da média mensal: {dias_acima_media}")
