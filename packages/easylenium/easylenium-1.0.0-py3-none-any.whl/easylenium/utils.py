import json
import logging
from typing import List, Dict, Union
from selenium import webdriver
from pathlib import Path

JsonType = Union[None, int, str, bool, List['JsonType'], Dict[str, 'JsonType']]


def create_chromedriver(download_directory: Union[str, Path],
                        open_pdf_externally: bool = True,
                        prompt_for_download: bool = False
                        ) -> webdriver.Chrome:
    """
    Create a Chrome WebDriver instance with customized download settings.

    Args:
        download_directory: The directory where downloaded files will be saved.
        open_pdf_externally: Whether to open PDF files externally 
            (default: True).
        prompt_for_download: Whether to prompt for download (default: False).

    Returns:
        webdriver.Chrome: The created Chrome WebDriver instance.

    """
    download_dir = (str(download_directory)
                    if isinstance(download_directory, Path)
                    else download_directory)
    preferences = {
        'download.default_directory': download_dir,
        "plugins.always_open_pdf_externally": open_pdf_externally,
        "download.prompt_for_download": prompt_for_download
    }
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', preferences)
    return webdriver.Chrome(options=options)


def file_exists(path: Path) -> bool:
    """
    Check if a file exists at the given path.

    Args:
        path (Path): The path to check.

    Returns:
        bool: True if a file exists at the given path, False otherwise.
    """
    return path.exists()


def save_to_json(data: JsonType, file_path: Path) -> bool:
    """
    Save data as JSON to the specified file.

    Args:
        data: The data to be saved as JSON.
        file_path: The path to the file where the JSON data will be saved.

    Returns:
        bool: True if the data is saved successfully.

    """
    logger = setup_logger("save")
    JSON_SUFFIX = ".json"
    
    if type(file_path) is not Path:
        file_path = Path(file_path)

    if file_path.suffix != JSON_SUFFIX:
        file_path = file_path.with_suffix(JSON_SUFFIX)

    logger.info(f"Saving file {file_path} as {JSON_SUFFIX} ...")
    with open(file_path, "w") as f:
        json.dump(data, f)
    logger.info(f"Finished saving file to {file_path}.")

    return file_exists(file_path)


def setup_logger(name: str) -> logging.Logger:
    """
    Creates a new logger with the specified name and 
    configures it to log messages to the console.

    Args:
        name: A string representing the name of the logger.

    Returns:
        A Logger object configured to log messages to the console 
        with a specific format.

    Example:
        >>> logger = setup_logger('my_logger')
        >>> logger.info('This is an information message')
        2023-05-07 09:35:22 INFO: This is an information message
    """
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)s: %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger
