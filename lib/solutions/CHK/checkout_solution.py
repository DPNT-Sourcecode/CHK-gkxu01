import re


def is_invalid_input(skus: str) -> bool:
    regex = re.compile('^[A-D]+$')
    return True if not regex.match(skus) else False


def item_price(sku: str):
    prices = {
        'A': { 'price': 50, 'special_offer': {'quantity': 3, 'price': 130} },
        'B': { 'price': 30, 'special_offer': {'quantity': 3, 'price': 130} },
        'C': { 'price': 20 },
        'D': { 'price': 15 },
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

    checkout_value = 0
    for item, amount in sku_dict.items():
        if item == 'A':
            special_offer_amount = amount / 3
            unique_amount = amount % 3




