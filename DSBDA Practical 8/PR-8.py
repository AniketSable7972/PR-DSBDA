# Name :- Aniket Sable
# Roll No. :- 54
# Class :- TE(IT)
# Practical 8 :- Create a review scrapper for any ecommerce website to fetch real time comments, reviews, ratings, comment tags, customer name using Python.

import requests                   # To handle HTTP requests (though not used in this script)
from bs4 import BeautifulSoup      # To parse HTML (also not used directly here)
from selenium import webdriver     # To automate browser actions
from selenium.webdriver.common.by import By  # To locate HTML elements
from selenium.webdriver.chrome.options import Options  # To configure ChromeDriver options
import pandas as pd                # To store and manipulate tabular data
import time                        # To introduce delays (wait for pages to load)

# Setup Chrome Driver with options
options = Options()
options.add_argument("--headless")  # Run browser in the background (no GUI)
options.add_argument("--disable-gpu")  # Disable GPU (optional for headless mode)

# Initialize the Chrome WebDriver with options
driver = webdriver.Chrome(options=options)

# Define user-agent headers (for requests, but not directly used in Selenium part)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}

# Function to scrape reviews from a Flipkart product page
def get_flipkart_reviews(product_url, max_pages=5):
    driver.get(product_url)  # Open the product page in Chrome
    time.sleep(3)            # Wait for the page to fully load

    reviews_list = []        # List to store all the reviews

    # Try to click on 'View All Reviews' button if present
    try:
        all_reviews_btn = driver.find_element(By.XPATH, "//div[contains(text(),'View all reviews')]")
        all_reviews_btn.click()
        time.sleep(2)
    except:
        print("Could not find 'View all reviews' button.")

    # Loop through the review pages (default max 5 pages)
    for page in range(max_pages):
        print(f"Scraping page {page + 1}")

        # Find all review blocks on the current page
        reviews = driver.find_elements(By.CLASS_NAME, "_16PBlm")
        for review in reviews:
            try:
                name = review.find_element(By.CLASS_NAME, "_2sc7ZR._2V5EHH").text   # Customer name
                rating = review.find_element(By.CLASS_NAME, "_3LWZlK").text         # Rating (stars)
                comment = review.find_element(By.CLASS_NAME, "t-ZTKy").text         # Comment text

                # Add extracted data to list
                reviews_list.append({
                    "Customer Name": name,
                    "Rating": rating,
                    "Comment": comment
                })
            except:
                continue  # Skip if any data is missing

        # Try to click on 'Next' button to go to the next page
        try:
            next_btn = driver.find_element(By.XPATH, "//span[contains(text(),'Next')]")
            next_btn.click()
            time.sleep(2)  # Wait for next page to load
        except:
            print("No more pages.")
            break  # Stop if no next button is found

    return reviews_list

# Product URL (iPhone 13 on Flipkart)
url = "https://www.flipkart.com/apple-iphone-13-blue-128-gb/p/itm6c601e0a58b3c?pid=MOBG6VF5SMXPNQHG..."

# Call the function to get reviews
reviews = get_flipkart_reviews(url, max_pages=10)  # Adjust max_pages if needed

# Convert the list of reviews into a DataFrame
df = pd.DataFrame(reviews)

# Save the DataFrame to a CSV file
df.to_csv("ecommerce_reviews.csv", index=False)
print("Reviews saved successfully!")
