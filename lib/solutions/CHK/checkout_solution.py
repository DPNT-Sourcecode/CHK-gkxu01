import re
from enum import Enum


class OfferType(Enum):
    MORE_FOR_LESS = 1
    FREE_ITEM = 2
    BUY_OF_GROUP = 3


def is_invalid_input(skus: str) -> bool:
    regex = re.compile('(^[A-Z]+$|^$)')
    return True if not regex.match(skus) else False


def get_sku_dict(skus: str) -> dict:
    sku_dict = {}
    for item in skus:
        if sku_dict.get(item) is not None:
            sku_dict[item] += 1
        else:
            sku_dict[item] = 1

    return sku_dict


def get_product_data(sku: str):
    prices = {
        'A': {
            'price': 50,
            'special_offers': [
                {'type': OfferType.MORE_FOR_LESS, 'quantity': 5, 'special_price': 200},
                {'type': OfferType.MORE_FOR_LESS, 'quantity': 3, 'special_price': 130},
            ],
        },
        'B': {
            'price': 30,
            'special_offers': [
                {'type': OfferType.MORE_FOR_LESS, 'quantity': 2, 'special_price': 45},
                {'type': OfferType.FREE_ITEM, 'quantity': 2, 'item': 'E'},
            ],
        },
        'C': {'price': 20},
        'D': {'price': 15},
        'E': {'price': 40},
        'F': {
            'price': 10,
            'special_offers': [
                {'type': OfferType.FREE_ITEM, 'quantity': 2, 'item': 'F', 'required_quantity': 3},
            ],
        },
        'G': {'price': 20},
        'H': {
            'price': 10,
            'special_offers': [
                {'type': OfferType.MORE_FOR_LESS, 'quantity': 10, 'special_price': 80},
                {'type': OfferType.MORE_FOR_LESS, 'quantity': 5, 'special_price': 45},
            ],
        },
        'I': {'price': 35},
        'J': {'price': 60},
        'K': {
            'price': 70,
            'special_offers': [
                {'type': OfferType.MORE_FOR_LESS, 'quantity': 2, 'special_price': 120},
            ],
        },
        'L': {'price': 90},
        'M': {
            'price': 15,
            'special_offers': [
                {'type': OfferType.FREE_ITEM, 'quantity': 3, 'item': 'N'},
            ],
        },
        'N': {'price': 40},
        'O': {'price': 10},
        'P': {
            'price': 50,
            'special_offers': [
                {'type': OfferType.MORE_FOR_LESS, 'quantity': 5, 'special_price': 200},
            ],
        },
        'Q': {
            'price': 30,
            'special_offers': [
                {'type': OfferType.MORE_FOR_LESS, 'quantity': 3, 'special_price': 80},
                {'type': OfferType.FREE_ITEM, 'quantity': 3, 'item': 'R'},
            ],
        },
        'R': {'price': 50},
        'S': {
            'price': 20,
            'special_offers': [
                {'type': OfferType.BUY_OF_GROUP, 'quantity': 3, 'special_price': 45, 'group': ['S', 'T', 'X', 'Y', 'Z']},
            ],
        },
        'T': {
            'price': 20,
            'special_offers': [
                {'type': OfferType.BUY_OF_GROUP, 'quantity': 3, 'special_price': 45, 'group': ['S', 'T', 'X', 'Y', 'Z']},
            ],
        },
        'U': {
            'price': 40,
            'special_offers': [
                {'type': OfferType.FREE_ITEM, 'quantity': 3, 'item': 'U', 'required_quantity': 4},
            ],
        },
        'V': {
            'price': 50,
            'special_offers': [
                {'type': OfferType.MORE_FOR_LESS, 'quantity': 3, 'special_price': 130},
                {'type': OfferType.MORE_FOR_LESS, 'quantity': 2, 'special_price': 90},
            ],
        },
        'W': {'price': 20},
        'X': {
            'price': 17,
            'special_offers': [
                {'type': OfferType.BUY_OF_GROUP, 'quantity': 3, 'special_price': 45, 'group': ['S', 'T', 'X', 'Y', 'Z']},
            ],
        },
        'Y': {
            'price': 20,
            'special_offers': [
                {'type': OfferType.BUY_OF_GROUP, 'quantity': 3, 'special_price': 45, 'group': ['S', 'T', 'X', 'Y', 'Z']},
            ],
        },
        'Z': {
            'price': 21,
            'special_offers': [
                {'type': OfferType.BUY_OF_GROUP, 'quantity': 3, 'special_price': 45, 'group': ['S', 'T', 'X', 'Y', 'Z']},
            ],
        },
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
        if offer2.get('type') == OfferType.MORE_FOR_LESS:
            price, paid_items_amount = calculate_more_for_less_offer_price(offer2, paid_items_amount)
            free_items_price += price

    return free_items_price, paid_items_amount


def calculate_buy_of_group_offer_price():
    pass


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if is_invalid_input(skus):
        return -1

    sku_dict = get_sku_dict(skus)
    item_total_price = {}
    groups = {}

    for sku, amount in sku_dict.items():
        item_total_price[sku] = 0
        product_data = get_product_data(sku)
        special_offers = product_data.get('special_offers')

        remaining_amount = amount
        if special_offers:
            for offer in special_offers:
                if offer.get('type') == OfferType.MORE_FOR_LESS:
                    price, remaining_amount = calculate_more_for_less_offer_price(offer, remaining_amount)
                    item_total_price[sku] += price
                elif offer.get('type') == OfferType.FREE_ITEM:
                    price, new_remaining_amount = calculate_free_items_offer_price(
                        offer, product_data, sku_dict, amount, special_offers,
                    )
                    if price is not None and (price <= item_total_price[sku] or item_total_price[sku] == 0):
                        item_total_price[sku] = price
                        remaining_amount = new_remaining_amount
                elif offer.get('type') == OfferType.BUY_OF_GROUP:
                    group: list[str] = offer.get('group', []).sort()
                    group_name = ''.join(group)
                    if groups.get(group_name):
                        groups[group_name] += amount
                    else:
                        groups[group_name] = amount
                    remaining_amount = 0

        if remaining_amount > 0:
            item_total_price[sku] += remaining_amount * product_data.get('price')

    for name, group in groups.items():


    return sum(item_total_price.values())




