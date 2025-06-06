import funcoes as f

posicao = ['-', '-', '-',
           '-', '-', '-',
           '-', '-', '-']


# Jogo
def jogo_rodando():

    flag = True                # Flag do loop principal
    trocar_jogador = True      # variavel Bool que muda para trocar jogador
    total_jogadas = 0          # Variavel para contar as jogadas serve para parar no empate
    jogadas_feitas = list()    # lista principal que salva jogadas feitas para evitar repetições

    while flag:

        # Mostrar tabuleiro

        f.tabuleiro(quadrantes=posicao)

        # Ficar intercalando entre os jogadores

        if trocar_jogador:
            simbolo = 'X'
        else:
            simbolo = 'O'
        trocar_jogador = not trocar_jogador

        #  LOOP escolhendo onde sera jogado SOMENTE SAI SE NÃO FOR REPETIDA POSIÇÃO
        flag_jogada = True
        while flag_jogada:                                                                # Subtrai por 1
            jogada = int(input('Escolha um número de 1 a 9 para começar a jogar: ')) - 1  # para ficar de 0-8

            # Evitar repetir mesmo quadrante em outra jogada
            # Ver se ja foi escolhido essa position
            if jogada in jogadas_feitas:
                print(f'Posição já foi escolhida, tente novamente')
            else:
                flag_jogada = False
            jogadas_feitas.append(jogada)

        # Adicionando e apagando antigos valores dentro da lista JOGADAS
        posicao.insert(jogada, simbolo)
        posicao.pop(1+jogada)

        # Finais do jogo

        # Vitoria caso qualquer um desses casos das funções retorne True
        if f.vitoria_horizontal(quadrantes=posicao) or f.vitoria_diagonal(quadrantes=posicao) or f.vitoria_vertical(quadrantes=posicao):
            print(f'Vitória do {simbolo}')
            f.tabuleiro(quadrantes=posicao)
            flag = False

        total_jogadas += 1

        # Caso empate

        if total_jogadas == 9:
            print('Empate')
            flag = False


jogo_rodando()
