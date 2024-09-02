import json
from pydantic import ValidationError
from custom_types import ScrapingConfig  # Import the Pydantic models
from scraper import scrape_page

# Load the JSON data
with open("selectors.json", "r") as file:
    data = json.load(file)

try:
    config = ScrapingConfig(**data)
except ValidationError as e:
    print("Configuration Error:", e.json())
    exit(1)

if __name__ == "__main__":
    scrape_page("login")  # Example: scrape the login page
