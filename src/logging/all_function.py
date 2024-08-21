import logging

# Configuração básica do logging
logging.basicConfig(level=logging.DEBUG,  # Defina o nível mínimo de log
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # Formato das mensagens
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def writelog(message):
    logger.debug(message)