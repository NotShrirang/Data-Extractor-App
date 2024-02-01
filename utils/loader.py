# Import necessary libraries
import json


def load_json(path) -> dict:
    """Function to load JSON file from given path

    Args:
        path (str): Path of the JSON file

    Returns:
        dict: dictionary of the data in the JSON file
    """
    with open(path, 'r') as f:
        return json.load(f)
