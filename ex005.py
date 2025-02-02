while True:
    # Entrada do usuário
    texto = input("Digite uma string (ou 'sair' para encerrar): ")

    # Verifica se o usuário deseja sair
    if texto.lower() == "sair":
        print("Programa encerrado.")
        break  # Sai do loop

    # Inverter a string manualmente
    invertida = ""
    for i in range(len(texto) - 1, -1, -1):
        invertida += texto[i]

    # Exibir o resultado
    print(f"String invertida: {invertida}\n")
