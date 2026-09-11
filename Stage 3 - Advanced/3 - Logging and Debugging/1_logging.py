import logging
import os
from logging.handlers import RotatingFileHandler

# logging is better than print in real projects

# log files go into a logs/ folder inside this script's folder
BASE = os.path.dirname(os.path.abspath(__file__))
LOGS = os.path.join(BASE, "logs")
os.makedirs(LOGS, exist_ok=True)


# basic levels - DEBUG INFO WARNING ERROR CRITICAL
logging.basicConfig(level=logging.DEBUG)

logging.debug("some detail")
logging.info("app started")
logging.warning("something odd")
logging.error("something failed")
logging.critical("very serious")


# with timestamp format
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

logging.info("user logged in")
logging.warning("disk space low")


# save logs to a file
file_handler = logging.FileHandler(os.path.join(LOGS, "app.log"))
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logging.getLogger().addHandler(file_handler)

logging.info("this also goes to app.log")
logging.error("error saved to file")


# use getLogger in real code not root logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.propagate = False

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
logger.addHandler(handler)

logger.info("started")
logger.debug("some debug info")
logger.warning("watch out")


# log to both console and file
myapp_log = os.path.join(LOGS, "myapp.log")

logger2 = logging.getLogger("myapp")
logger2.setLevel(logging.DEBUG)
logger2.propagate = False

fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

console_h = logging.StreamHandler()
console_h.setFormatter(fmt)

myapp_file_h = logging.FileHandler(myapp_log)
myapp_file_h.setFormatter(fmt)

logger2.addHandler(console_h)
logger2.addHandler(myapp_file_h)

logger2.info("goes to both places")
logger2.error("error in both")


# use exception() inside except - includes full traceback in log
def divide(a, b):
    try:
        return a / b
    except Exception:
        logging.exception("divide failed")

divide(10, 0)


# rotating log - stops file from growing too big
rot_log = os.path.join(LOGS, "rotating.log")
rot_handler = RotatingFileHandler(rot_log, maxBytes=1_000_000, backupCount=3)
rot_handler.setFormatter(fmt)

rot_logger = logging.getLogger("rotating")
rot_logger.addHandler(rot_handler)
rot_logger.setLevel(logging.INFO)
rot_logger.info("rotating log entry")


def calculate_salary(hours, rate):
    logging.info("salary calc started")
    logging.debug(f"hours={hours} rate={rate}")

    if hours < 0 or rate < 0:
        logging.warning("negative input given")
        raise ValueError("hours and rate must be positive")

    result = hours * rate
    logging.info(f"salary={result}")
    return result


try:
    print(calculate_salary(40, 500))
    print(calculate_salary(-5, 500))
except ValueError as e:
    logging.error(f"bad input: {e}")

print(f"\nlog files saved in: {LOGS}")
