import re
from enum import Enum


class OfferTypeEnum(Enum):
    MORE_FOR_LESS = 1
    FREE_ITEM = 2


def is_invalid_input(skus: str) -> bool:
    regex = re.compile('(^[A-E]+$|^$)')
    return True if not regex.match(skus) else False


def get_item_prices(sku: str):
    prices = {
        'A': {
            'price': 50,
            'special_offers': [
                {'type': OfferTypeEnum.MORE_FOR_LESS, 'quantity': 5, 'special_price': 200},
                {'type': OfferTypeEnum.MORE_FOR_LESS, 'quantity': 3, 'special_price': 130},
            ],
        },
        'B': {
            'price': 30,
            'special_offers': [
                {'type': OfferTypeEnum.MORE_FOR_LESS, 'quantity': 2, 'special_price': 45},
                {'type': OfferTypeEnum.FREE_ITEM, 'quantity': 2, 'item': 'E'},
            ],
        },
        'C': {'price': 20},
        'D': {'price': 15},
        'E': {
            'price': 40,
            # 'special_offers': [
            #     {'type': OfferTypeEnum.FREE_ITEM, 'quantity': 2, 'item': 'B'},
            # ],
        },
    }

    return prices.get(sku)


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if is_invalid_input(skus):
        return -1

    sku_dict = {}
    for item in skus:
        if sku_dict.get(item) is not None:
            sku_dict[item] += 1
        else:
            sku_dict[item] = 1

    item_total_price = {}
    for item, amount in sku_dict.items():
        item_total_price[item] = 0
        item_price = get_item_prices(item)
        special_offers = item_price.get('special_offers')

        remaining_amount = amount
        if special_offers:
            for offer in special_offers:
                if offer.get('type') == OfferTypeEnum.MORE_FOR_LESS:
                    quantity = offer.get('quantity')
                    if remaining_amount < quantity:
                        continue

                    special_offer_amount = remaining_amount // quantity
                    remaining_amount = remaining_amount % quantity

                    item_total_price[item] += special_offer_amount * offer.get('special_price')

        if remaining_amount > 0:
            item_total_price[item] += remaining_amount * item_price.get('price')

    return sum(item_total_price.values())



