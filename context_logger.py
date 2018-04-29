import json

from logging import LoggerAdapter, basicConfig, getLogger

DEFAULT_LOG_LEVEL = 'INFO'
LOG_FORMAT = dict(
    timestamp='%(asctime)s',
    level='%(levelname)s',
    module='%(name)s',
    version='%(version)s',
    user_id='%(user_id)s',
    request_id='%(request_id)s',
    trace_id='%(trace_id)s',
    message='%(message)s'
)


class ContextLogger(LoggerAdapter):
    version = ''
    user_id = ''
    request_id = ''
    trace_id = ''

    basicConfig(
        format=json.dumps(LOG_FORMAT),
        datefmt='%Y-%m-%dT%H:%M:%S.%f',
        level=DEFAULT_LOG_LEVEL
    )

    @staticmethod
    def get_logger(module_name):
        logger = getLogger(module_name)
        return ContextLogger(logger, {})

    @classmethod
    def context(cls, **kwargs):
        if 'ver' in kwargs:
            cls.version = kwargs['ver']

        if 'uid' in kwargs:
            cls.user_id = kwargs['uid']

        if 'rid' in kwargs:
            cls.request_id = kwargs['rid']

        if 'tid' in kwargs:
            cls.trace_id = kwargs['tid']

    def process(self, msg, kwargs):
        kwargs['extra'] = dict(
            version=ContextLogger.version,
            user_id=ContextLogger.user_id,
            request_id=ContextLogger.request_id,
            trace_id=ContextLogger.trace_id
        )
        return msg, kwargs

