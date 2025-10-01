# Função para exibir o tabuleiro
def mostrar_tabuleiro(tabuleiro):
    print("\nTabuleiro:")
    for linha in tabuleiro:
        for celula in linha:
            print(celula if celula != "" else "-", end=" ")
        print()

# Função para verificar vitória
def verificar_vitoria(tabuleiro, jogador):
    # Verifica linhas
    for linha in tabuleiro:
        if all(celula == jogador for celula in linha):
            return True
    # Verifica colunas
    for col in range(3):
        if all(tabuleiro[linha][col] == jogador for linha in range(3)):
            return True
    # Verifica diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True
    return False

# Função para verificar empate
def verificar_empate(tabuleiro):
    return all(celula != "" for linha in tabuleiro for celula in linha)

# Inicializa o tabuleiro vazio
tabuleiro = [["" for _ in range(3)] for _ in range(3)]
jogador_atual = "X"

# Loop principal do jogo
while True:
    mostrar_tabuleiro(tabuleiro)
    print(f"Jogador {jogador_atual}, sua vez.")
    
    try:
        linha = int(input("Digite a linha (0, 1 ou 2): "))
        coluna = int(input("Digite a coluna (0, 1 ou 2): "))
    except ValueError:
        print("Entrada inválida. Use números de 0 a 2.")
        continue

    if linha not in range(3) or coluna not in range(3):
        print("Posição fora do tabuleiro. Tente novamente.")
        continue

    if tabuleiro[linha][coluna] != "":
        print("Posição já ocupada. Tente novamente.")
        continue

    tabuleiro[linha][coluna] = jogador_atual

    if verificar_vitoria(tabuleiro, jogador_atual):
        mostrar_tabuleiro(tabuleiro)
        print(f"Jogador {jogador_atual} venceu!")
        break

    if verificar_empate(tabuleiro):
        mostrar_tabuleiro(tabuleiro)
        print("Empate!")
        break

    jogador_atual = "O" if jogador_atual == "X" else "X"
