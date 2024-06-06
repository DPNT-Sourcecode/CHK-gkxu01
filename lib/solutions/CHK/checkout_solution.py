import re


def is_invalid_input(skus: str) -> bool:
    regex = re.compile('^[A-D]+$')
    return True if not regex.match(skus) else False


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

    for item, amount in sku_dict.items():


