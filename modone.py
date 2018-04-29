from context_logger import ContextLogger

logger = ContextLogger.get_logger(__name__)


def do_something():
    logger.info('Inside do something')
    logger.debug('Debugging inside do something')
