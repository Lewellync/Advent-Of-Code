import logging.config

logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "standard",
            "stream": "ext://sys.stdout"
        }
    },
    "loggers": {
        "__main__":{
            "level": "INFO",
            "handlers": ["console"]
        },
        "root": {
            "level": "DEBUG",
            "handlers": ["console"]
        }
    }
}

logging.config.dictConfig(logging_config)