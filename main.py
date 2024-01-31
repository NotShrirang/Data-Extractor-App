import os
from PyPDF2 import PdfReader

from utils import download, fetch

path = os.path.dirname(os.path.abspath('__file__'))
url = 'https://assets.airtel.in/teams/simplycms/web/docs/Draft-Annual-Return-FY-2021-22.pdf'


def main():
    download.download_file(url, path)

    reader = PdfReader(url.split("/")[-1])

    for page in reader.pages[0:3]:
        text = " ".join(page.extract_text().split('\n'))
        print("CIN: "+str(fetch.get_cin(text)))
        print("EMAIL: "+str(fetch.get_email(text)))
        print("PAN: "+str(fetch.get_pan(text)))
        print("PHONE: "+str(fetch.get_phone(text)))


if __name__ == '__main__':
    main()
