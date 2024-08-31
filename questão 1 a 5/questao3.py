import json

faturamento_mensal = """
[
    {"dia": 1, "valor": 224.1},
    {"dia": 2, "valor": 245.68},
    {"dia": 3, "valor": 239.64},
    {"dia": 4, "valor": 0.0},
    {"dia": 5, "valor": 0.0},
    {"dia": 6, "valor": 262.66},
    {"dia": 7, "valor": 0.0},
    {"dia": 8, "valor": 429.58},
    {"dia": 9, "valor": 451.17},
    {"dia": 10, "valor": 191.2},
    {"dia": 11, "valor": 0.0},
    {"dia": 12, "valor": 0.0},
    {"dia": 13, "valor": 3.423},
    {"dia": 14, "valor": 373.38},
    {"dia": 15, "valor": 265.756},
    {"dia": 16, "valor": 48924.2448},
    {"dia": 17, "valor": 119.24},
    {"dia": 18, "valor": 0.0},
    {"dia": 19, "valor": 0.0},
    {"dia": 20, "valor": 350.26},
    {"dia": 21, "valor": 438.17},
    {"dia": 22, "valor": 182.68},
    {"dia": 23, "valor": 435.062},
    {"dia": 24, "valor": 127.125},
    {"dia": 25, "valor": 0.0},
    {"dia": 26, "valor": 0.0},
    {"dia": 27, "valor": 251.18},
    {"dia": 28, "valor": 178.1221},
    {"dia": 29, "valor": 130.495},
    {"dia": 30, "valor": 844.61}
]
"""

dados = json.loads(faturamento_mensal) # percorrer linha por linha nos dados

faturamentos = [dia["valor"] for dia in dados if dia["valor"] > 0 ] # para cada dia em dados se valor for maior que '0' adiciona ao faturamento


menor_valor = min(faturamentos) # faturamento minino

maior_valor = max(faturamentos) # faturamento maximo

media_mensal = sum(faturamentos) / len(faturamentos) # media do faturamento mensal

dias_acima_da_media = sum(1 for valor in faturamentos if valor > media_mensal)

print(f"Menor valor de faturamento ocorrido em um dia do mês: {menor_valor:.2f}")

print(f"Maior valor de faturamento ocorrido em um dia do mês: {maior_valor:.2f}")

print(f"Número de dias com faturamento diário superior à média mensal: {dias_acima_da_media}")