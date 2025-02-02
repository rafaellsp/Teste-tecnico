import json

# Ler o arquivo JSON
with open("faturamento.json", "r") as file:
    data = json.load(file)

# Extrair os valores de faturamento
faturamento_diario = data["faturamento"]

# Remover dias sem faturamento (valores 0)
dados_validos = [valor for valor in faturamento_diario if valor > 0]

# Verificar se há dados válidos
if not dados_validos:
    print("Nenhum dado de faturamento disponível para análise.")
else:
    # Cálculos
    menor_faturamento = min(dados_validos)
    maior_faturamento = max(dados_validos)
    media_mensal = sum(dados_validos) / len(dados_validos)
    dias_acima_da_media = sum(1 for valor in dados_validos if valor > media_mensal)

    # Exibir os resultados
    print(f"Menor faturamento diário: R$ {menor_faturamento:.2f}")
    print(f"Maior faturamento diário: R$ {maior_faturamento:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
