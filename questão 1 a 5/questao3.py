import json

with open("questão 1 a 5/dados.json", "r") as arquivo:

    resultado = arquivo.read()

    arquivo_json = json.loads(resultado) #arquivo json para manipulação

    faturamentos = [dia["valor"] for dia in arquivo_json if dia["valor"] > 0 ] # para cada dia em dados se valor for maior que '0' adiciona ao faturamento

    menor_valor = min(faturamentos) # faturamento minino

    maior_valor = max(faturamentos) # faturamento maximo

    media_mensal = sum(faturamentos) / len(faturamentos) # media do faturamento mensal

    dias_acima_da_media = sum(1 for valor in faturamentos if valor > media_mensal)

    print(f"Menor valor de faturamento ocorrido em um dia do mês: {menor_valor:.2f}")

    print(f"Maior valor de faturamento ocorrido em um dia do mês: {maior_valor:.2f}")

    print(f"Número de dias com faturamento diário superior à média mensal: {dias_acima_da_media}")