import re


def is_invalid_input(skus: str) -> bool:
    regex = re.compile('(^[A-D]+$|^$)')
    return True if not regex.match(skus) else False


def get_item_prices(sku: str):
    prices = {
        'A': {'price': 50, 'special_offer': {'quantity': 3, 'special_price': 130}},
        'B': {'price': 30, 'special_offer': {'quantity': 2, 'special_price': 45}},
        'C': {'price': 20},
        'D': {'price': 15},
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
        item_price = get_item_prices(item)
        special_offer = item_price.get('special_offer')

        if special_offer:
            quantity = special_offer.get('quantity')
            special_offer_amount = amount // quantity
            unique_amount = amount % quantity

            checkout_value += special_offer_amount * special_offer.get('special_price')
            checkout_value += unique_amount * item_price.get('price')
        else:
            checkout_value += amount * item_price.get('price')

    return checkout_value
