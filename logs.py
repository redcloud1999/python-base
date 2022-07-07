#!/usr/bin/env python3

import os
import logging
#BOILERPLATE
# TODO: usar função
# TODO: user lib (loguru)

log_level = os.getenv('LOG_LEVEL', 'WARNING').upper()

# nosa instancia de log
log = logging.Logger('logs',log_level)

# level
ch = logging.StreamHandler()
ch.setLevel(log_level)

# formatacao do logger
fmt = logging.Formatter(
    '%(asctime)s  %(name)s  %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)

# destino
log.addHandler(ch)

"""
log.debug('Mensagem pro dev, qe, sysadmin')
log.info('Mensagem geral para o usuário')
log.warning('Aviso que não causa erro')
log.error('Erro que afeta uma unica execução')
log.critical('Erro geral, ex: o banco de dados sumiu')
"""

print('____')

try:
    1 / 0

except ZeroDivisionError as e:
    log.error('Deu erro %s', str(e))














