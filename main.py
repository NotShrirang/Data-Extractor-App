# import necessary libraries
import os
import json
from PyPDF2 import PdfReader

from utils import download, fetch, loader

path = os.path.dirname(os.path.abspath('__file__'))


def main():
    data = loader.load_json('config.json')
    url = str(data['url'])

    if download.download_file(url, path):
        reader = PdfReader(url.split("/")[-1])

        with open('output.json', 'a') as f:
            f.write(r"{}")

        final_data = []
        for page_number, page in enumerate(reader.pages[0:data['page_count']]):
            text = " ".join(page.extract_text().split('\n'))

            cin = fetch.get_cin(text)
            print("CIN: " + str(cin))

            email = fetch.get_email(text)
            print("EMAIL: " + str(email))

            pan = fetch.get_pan(text)
            print("PAN: " + str(pan))

            phone_numbers = []
            mobile, landline, mobile_without_code = fetch.get_phone(text)
            print("PHONE: " + str(mobile), str(landline),
                  str(mobile_without_code))

            if len(mobile) != 0:
                phone_numbers.append(mobile)
            if len(landline) != 0:
                phone_numbers.append(landline)
            if len(mobile_without_code) != 0:
                phone_numbers.append(mobile_without_code)

            data = {
                "page": page_number+1,
                "data": {
                    "cin": cin,
                    "email": email,
                    "pan": pan,
                    "phone": phone_numbers
                }
            }
            final_data.append(data)

        with open("output.json", 'w') as f:
            json.dump(final_data, f, indent=4)
    else:
        print("An error occured. Please read the log file.")


if __name__ == '__main__':
    main()
