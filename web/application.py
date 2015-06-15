from web.controllers import app
from logging import getLogger

logger = getLogger(__name__)

if __name__ == '__main__':
    logger.info("Starting app")
    app.run()