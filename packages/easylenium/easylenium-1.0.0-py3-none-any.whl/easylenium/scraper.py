from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import (TimeoutException,
                                        NoSuchElementException,
                                        ElementClickInterceptedException)
from typing import Callable, List, Any, TypeVar, Optional, Union
from .utils import setup_logger
from .handler import handle
from .location import Location

T = TypeVar("T")
ExpectedCondition = Callable[[Location], Callable[[TypeVar("WebDriver")], Any]]
ElementGetter = Callable[[Location, ExpectedCondition], WebElement]

logger = setup_logger("scraper")

def no_such_element_handler(f) -> T: return handle(NoSuchElementException)(f)
def timeout_handler(f) -> T: return handle(TimeoutException)(f)


class Scraper:
    """
    Scraper class for web scraping using Selenium WebDriver.

    Args:
        driver: The WebDriver instance.
        timeout: The maximum time to wait for an element or condition 
            (default: 10 seconds).
        logger_name: The name of the Logger (default: "scraper")

    Attributes:
        driver: The WebDriver instance.
        wait: The WebDriverWait instance for waiting on conditions.
        logger: The Logger instance.

    """

    def __init__(self,
                 driver: webdriver.Chrome,
                 timeout: int = 10,
                 logger_name: str = "scraper"):
        self.driver = driver
        self.wait = WebDriverWait(driver=driver, timeout=timeout)
        self.logger = setup_logger(logger_name)

    @property
    def current_url(self) -> str:
        """
        Get the current URL of the web page.

        Returns:
            str: The current URL.

        """
        return self.driver.current_url

    def open_(self, url: str) -> bool:
        """
        Open the specified URL in the browser.

        Args:
            url: The URL to open.

        Returns:
            bool: True if the URL is opened successfully.

        """
        self.driver.get(url)
        return True

    def terminate(self) -> bool:
        """
        Quit the WebDriver and close the browser.

        Returns:
            bool: True if the WebDriver is terminated successfully.

        """
        self.driver.quit()
        return True

    @timeout_handler
    def wait_until_url_equals(self, url: str) -> bool:
        """
        Wait until the current URL equals the specified URL.

        Args:
            url: The URL to wait for.

        Returns:
            bool: True if the URL matches within the timeout.

        """
        self.wait.until(EC.url_to_be(url))
        return True

    @timeout_handler
    def wait_until_url_changes(self, url: str) -> str:
        """
        Wait until the current URL changes from the specified URL.

        Args:
            url: The URL to wait for the change.

        Returns:
            str: The updated current URL.

        """
        self.wait.until(EC.url_changes(url))
        return self.driver.current_url

    @timeout_handler
    def retrieve_element(self,
                         location: Location,
                         wait_for: ExpectedCondition
                         ) -> Union[Optional[WebElement],
                                    Optional[List[WebElement]]]:
        """
        Retrieve a single or multiple web elements matching the location.

        Args:
            location: The location of the element(s).
            wait_for: The expected condition to wait for.

        Returns:
            Union[Optional[WebElement], Optional[List[WebElement]]]: 
            The retrieved element(s) if found within the timeout, 
            otherwise None.

        """
        return self.wait.until(wait_for(location))

    @timeout_handler
    def get_element(self, location: Location) -> Optional[WebElement]:
        """
        Get a single web element matching the location.

        Args:
            location: The location of the element.

        Returns:
            Optional[WebElement]: The retrieved element if found within 
                the timeout, otherwise None.

        """
        return self.wait.until(EC.presence_of_element_located(location))

    @timeout_handler
    def get_elements(self, location: Location) -> Optional[List[WebElement]]:
        """
        Get multiple web elements matching the location.

        Args:
            location: The location of the elements.

        Returns:
            Optional[List[WebElement]]: The retrieved elements if found 
                within the timeout, otherwise None.

        """
        return self.wait.until(EC.presence_of_all_elements_located(location))

    @no_such_element_handler
    def search_for_elements_in_(self, element: WebElement, at: Location
                                ) -> List[WebElement]:
        """
        Search for web elements within a parent element.

        Args:
            element: The parent element to search within.
            at: The location of the elements relative to the parent element.

        Returns:
            List[WebElement]: The found web elements.

        """
        return element.find_elements(*at)

    @timeout_handler
    @no_such_element_handler
    def iterate_(self,
                 elements: List[WebElement],
                 apply_func: Callable[[WebElement], T]
                 ) -> List[T]:
        """
        Iterate over a list of web elements and apply a function 
        to each element.

        Args:
            elements: The list of web elements to iterate over.
            apply_func: The function to apply to each element.

        Returns:
            List[T]: The results of applying the function to each element.

        """
        return [apply_func(element) for element in elements]

    def click_(self, element: WebElement) -> WebElement:
        """
        Click on a web element.

        Args:
            element: The web element to click on.

        Returns:
            WebElement: The clicked web element.

        """
        element.click()
        return element

    def send_(self, keys: str, to: WebElement) -> WebElement:
        """
        Sends the specified keys to the given WebElement.

        Args:
            keys (str): The keys to send to the WebElement.
            to (WebElement): The target WebElement to send the keys to.

        Returns:
            WebElement: The same WebElement after sending the keys.

        """
        to.send_keys(keys)
        return to

    def prompt_for_(self, user_input_description: str) -> str:
        """
        Prompt the user for input.

        Args:
            user_input_description: The description of the input to prompt for.

        Returns:
            str: The user's input.

        """
        assert type(user_input_description) is str, "Please provide a str"
        return input(f"{user_input_description}: ")
