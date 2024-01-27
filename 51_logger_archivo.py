import logging
logging.basicConfig(filename='mi_registro.log',
                    level=logging.DEBUG, 
                    format=' %(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.debug('Este mensaje se guardara en archivo')
logger.info('Este mensaje se guardara en archivo')
