import logging

LOG_FORMAT = "%(levelname)s [%(asctime)s] (%(name)s:%(lineno)d) - %(message)s"


def config_main_logger(level:int, main_logger:str="") -> None:
    logger = logging.getLogger(main_logger)

    logger.setLevel(logging.NOTSET + 1)
    logger.propagate = False

    formatter = logging.Formatter(LOG_FORMAT)

    handler = logging.StreamHandler()
    handler.setLevel(level)
    handler.setFormatter(formatter)

    logger.addHandler(handler)
