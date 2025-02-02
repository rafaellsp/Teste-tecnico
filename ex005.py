# Entrada do usuário
texto = input("Digite uma string: ")

# Inverter a string manualmente
invertida = ""
for i in range(len(texto) - 1, -1, -1):
    invertida += texto[i]

# Exibir o resultado
print(f"String invertida: {invertida}")
