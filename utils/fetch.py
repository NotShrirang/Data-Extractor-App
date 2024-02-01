# Import necessary libraries
import re


def get_cin(text: str) -> list:
    """Function to get CINs present in the `text`

    Args:
        text (str): text to be searched

    Returns:
        list: list of CIN numbers found in the `text`.
    """
    return re.findall(r'[UL]\d{5}[a-zA-Z]{2}\d{4}[a-zA-Z]{3}\d{6}', text)


def get_email(text: str) -> list:
    """Function to get email present in the `text`

    Args:
        text (str): text to be searched

    Returns:
        list: list of email addresses found in the `text`
    """
    return re.findall(r'[\w\.-]+@[\w-]+\.[\w-]+', text)


def get_phone(text: str) -> tuple:
    """Function to get phone numbers present in the `text`

    Args:
        text (str): text to be searched

    Returns:
        tuple: tuple of phone numbers found in the `text`
    """
    mobile = re.findall(r'\+\d{12}', text)
    landline = re.findall(r'\d{11}', text)
    mobile_without_code = re.findall(r'\d{10}$', text)

    return mobile, landline, mobile_without_code


def get_pan(text: str) -> list:
    """Function to get PANs present in the `text`

    Args:
        text (str): text to be searched

    Returns:
        list: list of PANs found in the `text`
    """
    return re.findall(r'[a-zA-Z]{5}[0-9]{4}[a-zA-Z]{1}', text)
