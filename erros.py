#!/user/bin/env python3

import sys
import os

# testando se o arquivo realmente existe
if os.path.exists('names.txt'):
    print('O arquivo existe')
    input('...') # Race Condition
    names = open('names.txt').readlines()
else:
    print('[Error]: File names.txt not found')
    sys.exit(1)
        
# LBYL - Look Before You Leap

# testando se é possivel acessar o indice no arquivo
if len(names) >= 3:
    print(names[2])
else:
    print('[Error]: Missing name in the list')
    sys.exit(1)
