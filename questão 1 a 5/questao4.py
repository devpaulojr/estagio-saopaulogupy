faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
} # valores armazenados em um dicionário

faturamento_total = sum(faturamento_estados.values()) #cacular apenas os números dentro do dicionario

percentuais = {estado: (valor / faturamento_total) * 100 for estado, valor in faturamento_estados.items()} # Calcular o percentual de representação de cada estado

for estado , percentual in percentuais.items(): # para keys e values
    print(f"{estado}: {percentual:.2f}%")
