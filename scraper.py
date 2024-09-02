from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from main import config  # Import the validated config from main.py

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def get_page_content(page_key: str) -> str:
    root_url = config.pages.root
    page_path = getattr(config.pages, page_key, "/")
    full_url = root_url + page_path
    driver.get(full_url)
    return driver.page_source


def scrape_page(page_key: str):
    html_content = get_page_content(page_key)
    soup = BeautifulSoup(html_content, "html.parser")

    # Example: Scraping elements using CSS Selectors
    login_button_selector = config.selectors.cssSelectors.get("loginButton")
    login_button = soup.select_one(login_button_selector)
    if login_button:
        print("Login Button Text:", login_button.get_text())

    # Example: Scraping elements using XPath
    username_field_xpath = config.selectors.xPaths.get("usernameField")
    username_element = driver.find_element_by_xpath(username_field_xpath)
    if username_element:
        print(
            "Username Field Placeholder:", username_element.get_attribute("placeholder")
        )

    # Additional scraping logic...


if __name__ == "__main__":
    driver.quit()
