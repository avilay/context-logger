import logging
from context_logger import ContextLogger
from modone import do_something

logger = ContextLogger.get_logger(__name__)


def process(arg):
    logger.info(f'Inside process {arg}')


def main():
    logger.info('Starting example')
    process('before context')
    do_something()

    ContextLogger.context(uid=1000)
    process('after context')
    do_something()
    logger.info('After adding context')

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    ContextLogger.context(rid='hahaha')
    logger.debug('This is debug log')
    do_something()


if __name__ == '__main__':
    main()
