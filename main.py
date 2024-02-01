# import necessary libraries
import os
import sys
import timeit
import json
from PyPDF2 import PdfReader
from multiprocessing import Pool

from utils import download, fetch, loader, logger

PATH = os.path.dirname(os.path.abspath('__file__'))


def start_extraction(*args):
    url, page_count = args[0][0], args[0][1]
    if download.download_file(url, PATH):
        reader = PdfReader(url.split("/")[-1])
        final_data = []
        for page_number, page in enumerate(reader.pages[0:page_count]):
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
        return {url: final_data}
    else:
        print("An error occured. Please read the log file.")


def main():
    try:
        start_time = timeit.default_timer()
        json_data = loader.load_json('config.json')
        urls = json_data['urls']

        with open('output.json', 'w') as f:
            f.write(r"")

        if len(sys.argv) == 2:
            if sys.argv[1] == 'multiprocessing':
                final_result = {}
                with Pool() as pool:
                    results = pool.map(start_extraction, list([
                        (url, json_data['page_count'])
                        for url in urls
                    ]))

                for result in results:
                    key_name = list(result.keys())[0]
                final_result[key_name] = result[key_name]
            else:
                print("No Such Option!")
                return
        else:
            final_result = {}
            for url in urls:
                result = start_extraction((url, json_data['page_count']))
                final_result[url] = result[url]

        with open("output.json", 'w') as f:
            json.dump(final_result, f, indent=4)

        elapsed_time = timeit.default_timer() - start_time
        logger.log_message(
            message=f"Elapsed Time: {elapsed_time} seconds", level=0)
    except Exception as e:
        logger.log_message(e, level=1)


if __name__ == '__main__':
    main()
