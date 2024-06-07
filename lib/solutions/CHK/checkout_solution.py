import re
from enum import Enum


class OfferTypeEnum(Enum):
    MORE_FOR_LESS = 1
    FREE_ITEM = 2


def is_invalid_input(skus: str) -> bool:
    regex = re.compile('(^[A-F]+$|^$)')
    return True if not regex.match(skus) else False


def get_item_data(sku: str):
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
        'E': {'price': 40},
        'F': {
            'price': 10,
            'special_offers': [
                {'type': OfferTypeEnum.FREE_ITEM, 'quantity': 2, 'item': 'F', 'required_quantity': 3},
            ],
        },
        'G': {'price': 20},
        'H': {'price': 20},
        'I': {'price': 20},
        'J': {'price': 20},
        'K': {'price': 20},
        'L': {'price': 20},
        'M': {'price': 20},
        'N': {'price': 20},
        'O': {'price': 20},
        'P': {'price': 20},
        'Q': {'price': 20},
        'R': {'price': 20},
        'S': {'price': 20},
        'T': {'price': 20},
        'U': {'price': 20},
        'V': {'price': 20},
        'W': {'price': 20},
        'X': {'price': 20},
        'Y': {'price': 20},
        'Z': {'price': 20},
    }

    return prices.get(sku)


def calculate_more_for_less_offer_price(offer: dict, remaining_amount: int) -> tuple[int, int]:
    quantity = offer.get('quantity')
    if remaining_amount < quantity:
        return 0, remaining_amount

    special_offer_amount = remaining_amount // quantity
    new_remaining_amount = remaining_amount % quantity

    price = special_offer_amount * offer.get('special_price')

    return price, new_remaining_amount


def calculate_free_items_offer_price(offer: dict, item_data: dict, sku_dict: dict, amount: int, special_offers: list[dict]):
    offer_item = offer.get('item')
    offer_item_quantity = offer.get('quantity')
    minimal_quantity = offer.get('required_quantity')
    purchased_item_amount = sku_dict.get(offer_item)
    if not purchased_item_amount or (minimal_quantity and purchased_item_amount < minimal_quantity):
        return None, None

    if minimal_quantity:
        amount_left = purchased_item_amount - (purchased_item_amount // minimal_quantity)
        return amount_left * item_data.get('price'), 0

    free_items_quantity = purchased_item_amount // offer_item_quantity
    paid_items_amount = amount - free_items_quantity
    free_items_price = 0

    for offer2 in special_offers:
        if offer2.get('type') == OfferTypeEnum.MORE_FOR_LESS:
            price, paid_items_amount = calculate_more_for_less_offer_price(offer2, paid_items_amount)
            free_items_price += price

    return free_items_price, paid_items_amount


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
        item_data = get_item_data(item)
        special_offers = item_data.get('special_offers')

        remaining_amount = amount
        if special_offers:
            for offer in special_offers:
                if offer.get('type') == OfferTypeEnum.MORE_FOR_LESS:
                    price, remaining_amount = calculate_more_for_less_offer_price(offer, remaining_amount)
                    item_total_price[item] += price
                elif offer.get('type') == OfferTypeEnum.FREE_ITEM:
                    price, new_remaining_amount = calculate_free_items_offer_price(offer, item_data, sku_dict, amount, special_offers)
                    if price is not None and (price <= item_total_price[item] or item_total_price[item] == 0):
                        item_total_price[item] = price
                        remaining_amount = new_remaining_amount

        if remaining_amount > 0:
            item_total_price[item] += remaining_amount * item_data.get('price')

    return sum(item_total_price.values())

