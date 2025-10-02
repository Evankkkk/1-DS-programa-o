# Lista de desenhos da forca em etapas
desenhos = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

# Palavra secreta
palavra = "PYTHON"
letras_descobertas = ["_" for _ in palavra]
tentativas_restantes = 6
letras_erradas = []

# Loop principal
while tentativas_restantes > 0 and "_" in letras_descobertas:
    print(desenhos[6 - tentativas_restantes])
    print("Palavra:", " ".join(letras_descobertas))
    print("Letras erradas:", ", ".join(letras_erradas))
    print(f"Tentativas restantes: {tentativas_restantes}")
    
    palpite = input("Digite uma letra: ").upper()

    if palpite in palavra and palpite not in letras_descobertas:
        for i in range(len(palavra)):
            if palavra[i] == palpite:
                letras_descobertas[i] = palpite
    elif palpite in letras_erradas or palpite in letras_descobertas:
        print("Você já tentou essa letra.")
    else:
        letras_erradas.append(palpite)
        tentativas_restantes -= 1

# Resultado final
if "_" not in letras_descobertas:
    print("Parabéns! Você descobriu a palavra:", palavra)
else:
    print(desenhos[-1])
    print("Você perdeu! A palavra era:", palavra)
