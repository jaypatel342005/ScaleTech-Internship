import logging
import os

BASE = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(BASE, "logs"), exist_ok=True)
practice_log = os.path.join(BASE, "logs", "practice.log")

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(practice_log)
    ]
)

logger = logging.getLogger(__name__)


def calculate_discount(price, discount):
    logger.debug(f"price={price} discount={discount}")

    if price < 0:
        logger.warning("negative price")
        raise ValueError("price cant be negative")

    if discount < 0 or discount > 100:
        logger.warning(f"bad discount: {discount}")
        raise ValueError("discount must be 0-100")

    final = price - (price * discount / 100)
    logger.info(f"final={final}")
    return final


def process_order(items):
    logger.info(f"processing {len(items)} items")
    total = 0

    for item in items:
        try:
            price = calculate_discount(item["price"], item["discount"])
            total += price
        except ValueError as e:
            logger.exception(f"skipping {item['name']}: {e}")

    logger.info(f"total={total}")
    return total


orders = [
    {"name": "laptop",  "price": 50000, "discount": 10},
    {"name": "phone",   "price": 30000, "discount": 5},
    {"name": "tablet",  "price": -100,  "discount": 20},
    {"name": "charger", "price": 1500,  "discount": 150},
    {"name": "bag",     "price": 2000,  "discount": 15},
]

total = process_order(orders)
print(f"final total: {total}")

print(f"log saved to: {practice_log}")
