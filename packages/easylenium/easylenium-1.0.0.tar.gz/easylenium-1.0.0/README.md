# easylenium
A powerful web scraping tool for automating data extraction from websites using Selenium.

## Features
- Built on Selenium focusing on web scraping
- Reduce boilerplate and increase development speed
- Easily navigate web pages and interact with elements.
- Retrieve data from web pages using XPath or CSS selectors.
- Handle common scenarios like timeouts and missing elements.
- Support for multiple web browsers (Chrome, Firefox, Edge).
- Customizable options for handling downloads, prompts, and PDF files.

## Installation
You can install `easylenium` using pip:
```shell
pip install easylenium
```

Make sure you have Python 3.7 or above installed.

## Usage
```shell
from easylenium import (Scraper, create_chromedriver Location, By, save_to_json, handle)

# Create a scraper instance
driver = create_chromedriver("path/to/default/download/directory")
scraper = Scraper(driver)

# Open a web page
scraper.open_('https://example.com')

# Fill out form
example_textfield = scraper.get_element(Location(By.ID, "username_field"))
scraper.click_(example_textfield).send_keys("my_username")

# Interact with buttons
continue_button = scraper.get_element(Location(By.XPATH, "xpath/to/button"))
scraper.click_(continue_button)

# Find and retrieve elements
elements = scraper.get_elements(Location(By.CLASS_NAME, "bookItemTitle"))

# Write custom helper classes/functions
# (fully interactable with the python 'Selenium' package)
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException

@handle(NoSuchElementException)
def extract_url_from_(element: WebElement) -> str:
    return element.find_element(By.CLASS_NAME, 'a').get_attribute("href")

# Interact with elements, with optional handling of Exceptions
urls = scraper.iterate_(elements, extract_url_from_)

# Save data as json
save_to_json(urls, "path/to/save.json")

# Close the web scraper
scraper.terminate()
```

For more details and advanced usage examples, please refer to the documentation.

## Documentation
The complete documentation for easylenium can be found at (tbd).

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository (https://github.com/hubertus444/easylenium).

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Additional Info
The easylenium package provides a convenient and efficient 
way to perform web scraping and automate data extraction from websites.
It is built on top of the Selenium library, leveraging its capabilities 
to interact with web pages and extract desired data. 
With easylenium, you can easily navigate web pages, interact with elements, 
retrieve data, and handle common scenarios such as timeouts and 
missing elements. 
The package offers a high-level interface for common web scraping tasks, 
allowing you to focus on the data extraction process rather than 
the intricacies of web automation. 
Whether you need to scrape data for research, data analysis, or other purposes, 
easylenium simplifies the process and provides a reliable solution. 
It supports various web browsers, including Chrome, Firefox, and Edge, and 
provides customizable options for handling downloads, prompts, and PDF files. 
Empower your data extraction workflow with easylenium and 
unlock the potential of web scraping in Python.