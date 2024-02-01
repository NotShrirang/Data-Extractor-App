# import necessary libraries
import os
import json
from PyPDF2 import PdfReader

from utils import download, fetch, loader, logger

PATH = os.path.dirname(os.path.abspath('__file__'))


def main():
    try:
        json_data = loader.load_json('config.json')
        urls = json_data['urls']

        with open('output.json', 'w') as f:
            f.write(r"")

        final_dict = {}
        for url in urls:
            if download.download_file(url, PATH):
                reader = PdfReader(url.split("/")[-1])

                final_data = []
                for page_number, page in enumerate(reader.pages[0:json_data['page_count']]):
                    text = " ".join(page.extract_text().split('\n'))

                    cin = fetch.get_cin(text)
                    email = fetch.get_email(text)
                    pan = fetch.get_pan(text)
                    phone_numbers = []
                    mobile, landline, mobile_without_code = fetch.get_phone(
                        text)
                    dates = fetch.get_dates(text)
                    websites = fetch.get_websites(text)

                    if len(mobile) != 0:
                        phone_numbers.extend(mobile)
                    if len(landline) != 0:
                        phone_numbers.extend(landline)
                    if len(mobile_without_code) != 0:
                        phone_numbers.extend(mobile_without_code)

                    data = {
                        "page": page_number+1,
                        "data": {
                            "cin": cin,
                            "email": email,
                            "pan": pan,
                            "phone": phone_numbers,
                            "dates": dates,
                            "websites": websites
                        }
                    }

                    final_data.append(data)
                final_dict[url] = final_data
            else:
                print("An error occured. Please read the log file.")

        with open("output.json", 'w') as f:
            json.dump(final_dict, f, indent=4)
    except Exception as e:
        logger.log_message(e, level=1)


if __name__ == '__main__':
    main()
