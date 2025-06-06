def tabuleiro(quadrantes):
    print(f'{quadrantes[0]} | {quadrantes[1]} | {quadrantes[2]}\n'
          f'{quadrantes[3]} | {quadrantes[4]} | {quadrantes[5]}\n'
          f'{quadrantes[6]} | {quadrantes[7]} | {quadrantes[8]}')


def vitoria_horizontal(quadrantes):
    if quadrantes[0] == quadrantes[1] == quadrantes[2] != '-':
        return True
    elif quadrantes[3] == quadrantes[4] == quadrantes[5] != '-':
        return True
    elif quadrantes[6] == quadrantes[7] == quadrantes[8] != '-':
        return True


def vitoria_vertical(quadrantes):
    if quadrantes[0] == quadrantes[3] == quadrantes[6] != '-':
        return True
    elif quadrantes[1] == quadrantes[4] == quadrantes[7] != '-':
        return True
    elif quadrantes[2] == quadrantes[5] == quadrantes[8] != '-':
        return True


def vitoria_diagonal(quadrantes):
    if quadrantes[0] == quadrantes[4] == quadrantes[8] != '-':
        return True
    elif quadrantes[2] == quadrantes[4] == quadrantes[6] != '-':
        return True