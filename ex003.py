import json

# Carregar os dados do JSON
with open("dados.json", "r") as file:
    dados = json.load(file)

# Filtrar apenas os dias com faturamento acima de zero
faturamentos = [dia["valor"] for dia in dados if dia["valor"] > 0]

# Calcular menor e maior faturamento
menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)

# Calcular média mensal (ignorando dias sem faturamento)
media_mensal = sum(faturamentos) / len(faturamentos)

# Contar dias com faturamento acima da média
dias_acima_da_media = sum(1 for valor in faturamentos if valor > media_mensal)

# Exibir resultados
print(f"Menor faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior faturamento: R$ {maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")

# Função para inverter uma string
def inverter_string():
    while True:
        texto = input("Digite uma string (ou 'sair' para encerrar): ")
        if texto.lower() == "sair":
            print("Programa encerrado.")
            break
        invertida = ""
        for i in range(len(texto) - 1, -1, -1):
            invertida += texto[i]
        print(f"String invertida: {invertida}\n")

# Executar a função de inversão de string
inverter_string()
