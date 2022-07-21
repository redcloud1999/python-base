#!/usr/bin/env python3

import os
import logging
from logging import handlers

#BOILERPLATE
# TODO: usar função
# TODO: user lib (loguru)


# nivel de log pela variavel de ambiente
log_level = os.getenv('LOG_LEVEL', 'WARNING').upper()
# nossa instancia de log
log = logging.Logger('logs',log_level)
# level
# ch = logging.StreamHandler()  # Console/terminal/stderr
# ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(
    'meulog.log', 
    maxBytes=10**6,  # padrão 10**6 equiv 1mb
    backupCount=10,  # irá salvar os 10 ultimos arquivos de 100 bytes os anteriores serão apagados
)

fh.setLevel(log_level)

# formatacao do logger
fmt = logging.Formatter(
    '%(asctime)s  %(name)s  %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
fh.setFormatter(fmt)
# destino
log.addHandler(fh)


"""
log.debug('Mensagem pro dev, qe, sysadmin')
log.info('Mensagem geral para o usuário')
log.warning('Aviso que não causa erro')
log.error('Erro que afeta uma unica execução')
log.critical('Erro geral, ex: o banco de dados sumiu')
"""

try:
    1 / 0

except ZeroDivisionError as e:
    log.error('Deu erro %s', str(e))














