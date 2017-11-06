import logging


from taxclock.settings import LOGGING, SLACK_WEBHOOK
from slack_logger import SlackHandler, SlackFormatter

# Set up logging


sh = SlackHandler(username='Taxclock Scraper Logger', url=SLACK_WEBHOOK)
sh.setLevel('DEBUG')
f = SlackFormatter()
sh.setFormatter(f)

def set_logging(level=logging.INFO):
    '''
      Handles both logging to file and slack.
    '''
    try:
        logging.config.dictConfig(LOGGING)
    except Exception as err:
        logging.basicConfig(level=level)

    log = logging.getLogger(__name__)
    log.setLevel('INFO')
    log.addHandler(sh)
    return log
