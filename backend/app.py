import logging.config
from molten import App, Route

logging.config.dictConfig({
    "version": 1,
    "filters": {
        "request_id": {
            "()": "molten.contrib.request_id.RequestIdFilter"
        },
    },
    "formatters": {
        "standard": {
            "format": "%(levelname)-8s [%(asctime)s] [%(request_id)s] %(name)s: %(message)s"
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "filters": ["request_id"],
            "formatter": "standard",
        },
    },
    "loggers": {
        "myapp": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
    }
})



def hello(name: str) -> dict:
    logging.debug(f'hi there {name}')
    return {"message": f"Hello {name}!", "is_superuser": True, "name": f"{name}"}

def data() -> dict:
    logging.debug('got list request')
    return {"results": [{"num": i} for i in range(0, 3)]}

def list_data() -> list:
    logging.debug('got list request')
    return [{"list_data": i} for i in range(0, 5)]

routes = [
    Route("/hello/{name}", hello),
    Route("/test/data/", data),
    Route("/test/list_data/", list_data),
]

app = App(routes=routes)