import random

numero_secreto = random.randint(1, 20)
palpite = None
tentativas = 0

# Repete enquanto o palpite estiver errado e o limite de tentativas não for atingido
while palpite != numero_secreto and tentativas < 5:
    palpite = int(input("Adivinhe o número (1 a 20): "))
    tentativas += 1

    if palpite == numero_secreto:
        print("🎉 Acertou!")
    else:
        print("❌ Tente novamente.")

if palpite != numero_secreto:
    print(f"💀 Fim de jogo! O número era {numero_secreto}.")
