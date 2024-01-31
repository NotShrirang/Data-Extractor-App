import re


def get_cin(text: str) -> str:
    return re.search(r'[UL]\d{5}[a-zA-Z]{2}\d{4}[a-zA-Z]{3}\d{6}', text).group().split()[-1]
