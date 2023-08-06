import logging
import sys

loggers = {}
# This function is used to create logging configiration
def project_logger(name):
    if loggers.get(name):
        return loggers.get(name)
    else:
        # create logger
        logger = logging.getLogger(name)
        logger.setLevel(level=logging.DEBUG)

        logStreamFormatter = logging.Formatter(
        fmt=f"%(levelname)-8s %(asctime)s \t %(filename)s @function %(funcName)s line %(lineno)s - %(message)s", 
        datefmt="%H:%M:%S"
        )
        consoleHandler = logging.StreamHandler(stream=sys.stdout)
        consoleHandler.setFormatter(logStreamFormatter)
        consoleHandler.setLevel(level=logging.DEBUG)
        logger.addHandler(consoleHandler)

        # set formatter
        logFileFormatter = logging.Formatter(
            fmt=f"%(levelname)-8s %(asctime)s \t %(filename)s @function %(funcName)s line %(lineno)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        # set the handler
        fileHandler = logging.handlers.RotatingFileHandler(filename='logdir/log_file.log', maxBytes=1000_000, backupCount=3)
        fileHandler.setFormatter(logFileFormatter)
        fileHandler.setLevel(level=logging.DEBUG)
        logger.addHandler(fileHandler)
        
        loggers[name] = logger
        
        return logger