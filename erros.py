#!/user/bin/env python3

import sys
import os

# EAFP - Easy to Ask Forgiveness than permission
# (É mais fácil pedir perdão do que permissão)


try:
    names = open('names.txt').readlines()  # FileNotFoundError

except FileNotFoundError as e: # Bare except
    print(f'Erro: {str(e)}')
    sys.exit(1)
    # TODO: Usar retry
else:
    print('Sucesso!!!')
finally:
    print('sempre execute isso!')


try:
    print(names[2])
except:
    print('[Error]: Missing name in the list')
    sys.exit(1)


