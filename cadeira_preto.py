# -*- coding: utf-8 -*-
# author: <nome>
# date: <data>
# description: <desc>
# license: <license>

"""
    docstring
"""

# Cabeçalhos: são linhas de comentários do topo do arquivo, usado para descrever e fornecer informações para o desenvolvedor.
# Não é extritamente necessários, mas é uma boa prática utilizar.

"""
    Docstrings são uma forma de documentação incorporada ao código, elas são colocadas logo após a definição de funções,
    métodos ou classes, e servem para descrever o que eles fazem.
"""


# Objetivo: praticar if/else, loops e erros.

def e_par(n: int) -> bool:
    """Retorna True se n é par, senão False."""
    # TODO: retorne se n é par
    """
    if n % 2 == 0 :
        return true
    else:
        return false
    """
    return n % 2 == 0
    ...

def fatorial(n: int) -> int:
    """Retorna n! (n fatorial). Para n<0, levante ValueError."""
    # TODO: implemente de forma iterativa (sem recursão)
    aux = 1
    for i in range(1, n) :
        aux = aux * (i + 1)

    return aux
    ...

def maximo(nums):
    """Retorna o maior elemento de uma lista não vazia, sem usar max()."""
    # TODO: percorra a lista guardando o maior atual
    try:
        if len(nums) == 0 :
            raise ValueError
    except ValueError:
        print('An empty array was provided.')
    else:
        aux = nums[0]
        for i in range(0, len(nums)):
            if aux < nums[i] :
                aux = nums[i]
        
        return aux
    ...


print(e_par(3))
print(fatorial(5))
print(maximo([12, 0, 17, 28, 39]))
maximo([])
