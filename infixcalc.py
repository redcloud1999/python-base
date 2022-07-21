#!/usr/bin/env python3

'''Calculadora infix

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5
50

$ infixcalc.py
operação: sum
n1: 5
n2: 4
9


OS resultados serão salvos em infixcalc.log
'''
__version__ = '0.1.0'

import logging
from logging import handlers
import sys
import os
from datetime import datetime


log_level = os.getenv('LOG_LEVEL', 'DEBUG')
log = logging.Logger('infixcalc_log', log_level)
impress = handlers.RotatingFileHandler(
    'infixcalc.log',
    maxBytes=10**6,
    backupCount=15,
)
impress.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s  %(name)s  %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
impress.setFormatter(fmt)
log.addHandler(impress)


# programa em si
arguments = sys.argv[1:]


while True:
    arguments = sys.argv[1:]
    # validação
    if not arguments:
        operation = input('Insira a operação sum, sub, mul ou div: ')
        n1 = input('n1: ')
        n2 = input('n2: ')
        arguments = [operation, n1, n2]
        
    elif len(arguments) != 3:
        print('Numero de argumentos inválido')
        print('ex: `sum 5 5`')
        sys.exit(1)

    operation, *nums = arguments

    valid_operations = ('sum', 'sub', 'mul', 'div')
    if operation not in valid_operations:
        print('Operação inválida')
        print(valid_operations)
        sys.exit(1)

    validated_nums = []
    for num in nums:
        if not num.replace('.', '').isdigit():
            print(f'Numero inválido {num}')
            sys.exit(1)
        if '.' in num:
            num = float(num)
        else:
            num = int(num)
        validated_nums.append(num)
    try:

        n1, n2 = validated_nums
    except ValueError as e:
        print(f'{str(e)}')
    if operation == 'sum':
        result = n1 + n2
    elif operation == 'sub':
        result = n1 - n2
    elif operation == 'mul':
        result = n1 * n2
    elif operation == 'div':
        result = n1 / n2


    path = '/'
    filepath = os.path.join(path, 'infixcalc.log')
    timestamp = datetime.now().isoformat()
    user = os.getenv('USER', 'anonymous')

    print(f'O resultado é {result}')

    try:
        with open(filepath, 'a') as file_:
            file_.write(f'{timestamp} - {user} {operation}, {n1}, {n2} = {result}\n')
    except PermissionError as e:
        log.error('Deu erro: %s', str(e))
        sys.exit(1)

    if input('\nPressione enter para efetuar outra operações \nqualquer tecla para sair'):
        break

















