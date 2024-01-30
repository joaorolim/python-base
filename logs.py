#!/usr/bin/env python3

# ./logs.py 2&>> /tmp/logs/error.log
# ./logs.py 1&>> /tmp/logs/error.log
# 1 / 0

import os
import logging



logging.debug("Mensagem para o DEV, QA, SYSADMIN")
logging.info("Mensagem geral para usuários")
logging.warning("Aviso que não causa erro - ex: funções que serão desabilitadas")
logging.error("Erro que afeta um única execução - ex: user sem permissão")
logging.critical("Erro geral - ex: banco de dados sumiu")

print("-" * 80)

# BOILERPLATE
# TODO: usar função
# TODO: usar lib externa (loguru)

log_level =os.getenv("LOG_LEVEL", "WARNING").upper()
# nossa instancia
log = logging.Logger("mainLog", log_level)
# level
ch = logging.StreamHandler()  # console handler -> o StreamHandler manda para o console/terminal/stderr
ch.setLevel(log_level)
# formatação
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
# destino
log.addHandler(ch)


log.debug("Mensagem para o DEV, QA, SYSADMIN")
log.info("Mensagem geral para usuários")
log.warning("Aviso que não causa erro - ex: funções que serão desabilitadas")
log.error("Erro que afeta um única execução - ex: user sem permissão")
log.critical("Erro geral - ex: banco de dados sumiu")

print("-" * 80)

try:
    1 / 0
except ZeroDivisionError as e:
    print(f"[Error] {str(e)}")

