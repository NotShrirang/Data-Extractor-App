import re


def get_cin(text: str) -> list:
    return re.findall(r'[UL]\d{5}[a-zA-Z]{2}\d{4}[a-zA-Z]{3}\d{6}', text)


def get_email(text: str) -> list:
    return re.findall(r'[\w\.-]+@[\w-]+\.[\w-]+', text)


def get_phone(text: str) -> list:
    phone3 = re.findall(r'\+\d{12}', text)
    phone2 = re.findall(r'\d{11}', text)
    phone1 = re.findall(r'\d{10}$', text)

    return phone1, phone2, phone3


def get_pan(text: str) -> list:
    return re.findall(r'[a-zA-Z]{5}[0-9]{4}[a-zA-Z]{1}', text)
