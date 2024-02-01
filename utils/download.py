# Import necessary libraries
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import logger


def download_file(url: str, dir: str) -> bool:
    """Function for downloading the PDF

    Args:
        url (str): URL of the PDF
        dir (str): path of the directory in which PDF should be stored

    Returns:
        bool: `True` if PDF is downloaded else `False`.
    """
    try:
        # Load webdriver
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('prefs', {'plugins.always_open_pdf_externally': True, "directory_upgrade": True, "safebrowsing.enabled": False,
                                                         "download.default_directory": dir})
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)

        # Wait till elements are loaded and then click the element.
        WebDriverWait(driver, 1).until(EC.element_to_be_clickable(
            (By.XPATH, r"/html/body/pdf-viewer/viewer-toolbar/div/div[3]/viewer-download-controls/cr-icon-button"))).click()
        driver.close()
        logger.log_message("Success", level=0)
        return True
    except TimeoutException as e:
        logger.log_message(f"TimeOutException: {e.args}", level=1)
        return True

    except Exception as e:
        logger.log_message(f"Error: {e.args}", level=1)
        return False
