import re

def is_invalid_input(skus: str) -> bool:
    regex = re.compile('^[A-D]+$')
    return True if not regex.match(skus) else False

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
