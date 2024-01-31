import re


def get_cin(text: str) -> str:
    return re.search(r'\(CIN\) of the company [0-9a-zA-Z]{21}', text).group().split()[-1]
