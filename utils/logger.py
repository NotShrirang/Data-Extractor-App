# import necessary libraries
import logging


def log_message(message: str, level: int):
    """
    logs success/failure messages in logger file

    Args:
        message (str): message to log
        level (int): severity level (error=1, info=0)

    Returns:
        pd.DataFrame: will later be converted into csv
    """
    # Configuring basic logging settings
    logging.basicConfig(filename='logger.log',
                        format="%(asctime)s - %(levelname)s - %(message)s",
                        level=logging.INFO)

    # Logging based on severity level
    if level == 1:
        logging.error(message)
    elif level == 0:
        logging.info(message)
