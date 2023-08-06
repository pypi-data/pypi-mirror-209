import collections
from selenium.webdriver.common.by import By


class Location(collections.Sequence):
    """
    Custom class representing a location in Selenium WebDriver.

    Args:
        locator: The locator strategy to use (e.g., By.ID, By.XPATH, etc.).
        location_value: The value of the locator.

    Attributes:
        tup: A tuple representing the locator and its value.

    """

    def __init__(self, locator: By, location_value: str):
        self.tup = (locator, location_value)

    def __len__(self):
        return len(self.tup)

    def __getitem__(self, index):
        return self.tup[index]
