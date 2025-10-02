
24/09-PRÁTICA: estruturas de repetição avançadas
fabricio.west@escola.pr.gov.br Mudar de conta
 
Rascunho salvo.
* Indica uma pergunta obrigatória
Enviar por e-mail
*
Registrar fabricio.west@escola.pr.gov.br como o e-mail a ser incluído na minha resposta
0. Escreva o seu nome
fabricio
1. LOOPS ANINHADOS são estruturas de repetição onde um loop está dentro de outro loop, como no código da imagem.

São úteis quando se precisa trabalhar com dados organizados em duas dimensões, como matrizes, tabelas, ou listas de listas.  

Execute o exemplo de código da imagem no editor Programiz e marque todas as afirmativas corretas sobre a saída da execução.
*
4 pontos
Imagem sem legenda
Os loops aninhados organizam e formatam a impressão dos preços por loja em uma estrutura visual confusa.
O loop externo "for i in range(len(lojas))" percorre a lista de lojas e imprime o nome de cada uma.
O loop interno "for preco in precos[i]" percorre a lista de preços da loja atual e os exibe com "R$" e 2 casas decimais.
Os loops aninhados criam uma estrutura visual semelhante a um gráfico simples.
2. Jogo da Velha em Python
Objetivo: Crie um jogo da velha simples para dois jogadores no terminal do computador em linguagem Python.

Requisitos:

- Use uma matriz 3x3 para representar o tabuleiro.

- Mostre o tabuleiro usando loops aninhados (um loop dentro de outro).

- Os jogadores alternam entre "X" e "O".

- Cada jogada deve pedir linha e coluna via input().

- Verifique vitória por linhha, coluna ou diagonal.

- Declare empate se todas as posições forem preenchidas sem vencedor.

Dica: Organize o código com funções e valide se a posição está livre antes de jogar.

Copie abaixo o seu código do jogo da velha.

*
4 pontos
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

3. Teste do jogo da velha
Execute o código do seu jogo da velha no editor Programiz para Python, desse modo:

- Acesse o editor e apague tudo que está na tela.
- Copie/cole o seu código do jogo.
- Clique no botão azul "Run" para executar.
- Jogue junto com um colega até finalizar.
- Corrija erros, se houver, e execute de novo.

Copie o link da execução correta do jogo da velha no Programiz (use o botão "Share").
*
10 pontos
Imagem sem legenda
https://www.programiz.com/online-compiler/7J8nCTVwZ7WYW
4. LOOPS COM MÚLTIPLAS CONDIÇÕES são estruturas de repetição que avaliam mais de uma condição lógica para decidir se continuam executando ou não. 

São úteis quando se precisa que vários critérios sejam atendidos ao mesmo tempo (ou que pelo menos um deles seja) para manter o loop ativo.

Execute o exemplo de código da imagem no editor Programiz e marque apenas as afirmativas incorretas sobre este programa.
*
4 pontos
Imagem sem legenda
O loop while utiliza múltiplas condições com o operador "and".
O loop continua enquanto o palpite estiver errado e o nº de tentativas for menor que 5.
O número secreto é revelado a cada tentativa, independentemente do palpite.
O código utiliza um loop for para limitar as tentativas do jogador.
5. Sistema de Login com tempo e tentativas
Objetivo: Crie um sistema de login simples em Python que permita ao usuário digitar a senha dentro de um limite de tempo e nº de tentativas.

Requisitos:

- Defina uma senha fixa no código (ex: "1234").

- O usuário tem até 3 tentativas para acertar a senha.

- O tempo total para tentar o login é de 30 segundos.

- Use a função time.time() para medir o tempo decorrido desde o início da sessão.

- Use um loop com múltiplas condições: o loop deve continuar enquanto o número de tentativas for maior que zero e o tempo não tiver expirado.

- A cada tentativa: solicite a senha com input(); verifique se está correta; se estiver correta, use break para encerrar o loop; se estiver incorreta, reduza o nº de tentativas e informe ao usuário.

- Após o loop, verifique se o acesso foi negado por erro ou por tempo expirado, e exiba a mensagem correspondente.

Copie abaixo o seu código do sistema de login.

*
4 pontos
import time

# Senha fixa
senha_correta = "1234"

# Configurações
tentativas = 3
tempo_limite = 30  # segundos
inicio = time.time()
acesso_liberado = False

# Loop com múltiplas condições
while tentativas > 0 and (time.time() - inicio) < tempo_limite:
    entrada = input("Digite a senha: ")

    if entrada == senha_correta:
        acesso_liberado = True
        break
    else:
        tentativas -= 1
        print(f"Senha incorreta. Tentativas restantes: {tentativas}")

# Verificação final
tempo_total = time.time() - inicio

if acesso_liberado:
    print("✅ Acesso liberado!")
elif tentativas == 0:
    print("❌ Acesso negado: número de tentativas excedido.")
elif tempo_total >= tempo_limite:
    print("⏰ Acesso negado: tempo expirado.")

6. Teste do sistema de login 
Execute o código do sistema de login no editor Programiz para Python, desse modo:

- Acesse o editor e apague tudo que está na tela.
- Copie/cole o seu código do sistema.
- Clique no botão azul "Run" para executar.
- Responda o que o sistema pedir até finalizar.
- Corrija erros, se houver, e execute de novo.

Copie o link da execução correta do sistema de login no Programiz (use o botão "Share").
*
9 pontos
Imagem sem legenda
https://www.programiz.com/online-compiler/5S54sHNdd6kcD
7. LOOP COM CONTROLE DE FLUXO usa comandos como if, break ou continue dentro do corpo do loop.
Esses comandos alteram o comportamento da repetição conforme condições específicas. Isso permite interromper, pular ou adaptar o loop durante sua execução.

Execute o exemplo de código da imagem no editor Programiz e marque apenas as afirmativas incorretas sobre este programa.

*
4 pontos
Imagem sem legenda
O jogador vê a palavra oculta como uma sequência de traços, atualizada a cada acerto.
O jogo revela todas as letras da palavra no início para facilitar a adivinhação.
O jogo informa se a letra está certa ou errada e mostra o nº de tentativas restantes.
O jogador pode digitar várias letras ao mesmo tempo para acelerar o jogo.
O comando break é usado para encerrar o loop se o jogador desiste ou descobre a palavra.
8. Ampliação do Jogo da Forca: Desenho do Boneco
Objetivo: melhorar o jogo da forca existente, adicionando representação visual do boneco sendo montado a cada erro do jogador.

Requisitos adicionais:

- Mantenha o código original do jogo da forca.

- Crie uma lista com desenhos da forca, divididos em etapas (cabeça, corpo, braços, pernas).

- A cada erro, exiba o desenho correspondente ao número de tentativas restantes.

- Mostre o boneco completo quando o jogador perder o jogo.

Dica: Use uma lista de strings com os desenhos e acesse o índice com base no número de erros cometidos.

Copie abaixo o seu código ampliado do jogo da forca.

*
4 pontos
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

9. Teste do jogo da forca com boneco 
Execute o código do sistema de login no editor Programiz para Python, desse modo:

- Acesse o editor e apague tudo que está na tela.
- Copie/cole o seu código do jogo.
- Clique no botão azul "Run" para executar.
- Jogue até finalizar.
- Corrija erros, se houver, e execute de novo.

Copie o link da execução correta do jogo da forca ampliado no Programiz (use o botão "Share").
*
9 pontos
Imagem sem legenda
https://www.programiz.com/online-compiler/37Dmp37doOYrl
10. Salve os códigos desta prática no repositório de Lógica Computacional do seu GitHub.

- Use estes nomes para salvar os arquivos separadamente:
tabela-precos.py
jogo-da-velha.py
jogo-de-adivinhacao.py
sistema-login.py
jogo-da-forca1.py
jogo-da-forca2.py

- Abra o repositório de lógica.
- Clique em Add file/Create new file.
- Digite o nome do arquivo no campo previsto.
- Copie o código na área Edit.
- Confirme 2 x no botão verde Commit.
- Abra o arquivo novo.

Copie abaixo os 6 links dos arquivos armazenados no seu GitHub.
*
28 pontos
https://github.com/Evankkkk/1-DS-programa-o/blob/main/tabela-precos.py                            https://github.com/Evankkkk/1-DS-programa-o/blob/main/jogo-da-velha.py                https://github.com/Evankkkk/1-DS-programa-o/blob/main/jogo-de-adivinhacao.py         
Uma cópia das suas respostas será enviada por e-mail para fabricio.west@escola.pr.gov.br.
Página 1 de 1
Nunca envie senhas pelo Formulários Google.
Este formulário foi criado em SEED. - Entre em contato com o proprietário do formulário
Google Formulários
