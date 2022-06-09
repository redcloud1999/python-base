#!/usr/bin/env python3


"""Hello World Multi Linguas.


Dependendo da lingua configurada no
ambienteo programa exibe a mensagem
 correspondente.

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR


Execução:

    python3 hello.py
    ou
    ./hello.py

"""

__version__ = "0.0.1"
__author__ = "Otávio Trindade"
__licence__ = "Unlicense"


import os

current_language = os.getenv("LANG", "en_EN")[:5]

msg = {
    'en_EN': 'Hello, World!',
    'pt_BR': 'Olá, Mundo!',
    'it_IT': 'Ciao, Mondo!',
    'fr_FR': 'Bonjour, Monde!',    
}






print(msg[current_language])



