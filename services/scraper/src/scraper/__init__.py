"""Application entrypoint for the scraper service."""

import logging
import time


logger = logging.getLogger(__name__)


def main() -> None:
    """Start the scraper process.

    The worker loop is intentionally minimal until the scraping scheduler is
    wired in. Keeping the process alive makes the container lifecycle correct.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    logger.info("Scraper is running normally")

    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        logger.info("Scraper is shutting down")


if __name__ == '__main__':
    main()
