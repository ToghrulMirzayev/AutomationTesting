import inspect
import logging as log

# class for logs collection
class Utils:
    def custom_logger(logLevel=log.INFO):
        logger_name = inspect.stack()[1][3]

        logger = log.getLogger(logger_name)
        logger.setLevel(logLevel)

        fh = log.FileHandler('logfile.log')

        formatter = log.Formatter("%(asctime)s - %(levelname)s - %(message)s", datefmt='%m/%d/%Y %I: %M: %S %p')

        fh.setFormatter(formatter)

        logger.addHandler(fh)
        return logger
