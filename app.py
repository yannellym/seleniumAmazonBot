from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

import time
from tabulate import tabulate


# python3 -m venv venv
# source venv/bin/activate

# select the driver
driver = webdriver.Chrome()

# Access Google
driver.get("https://www.google.com/")
# get the searchbar id
google_searchbar_id = "APjFqb"

# wait until we have the element on the page
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, google_searchbar_id))
)
# find the element
input_element = driver.find_element(By.ID, google_searchbar_id)
# append the string
input_element.send_keys("Amazon" + Keys.ENTER)
# find the partial text
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Amazon.com")
# click on it
link.click()

# Maximize the window
driver.maximize_window()

# Locate and click on the "Today's Deals" link by its href attribute
todays_deals_link = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/deals?ref_=nav_cs_gb']"))
)
todays_deals_link.click()

# Wait for the checkbox to be clickable
checkbox = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox'][@data-csa-c-element-id='filter-department-541966']"))
)
# Click on the checkbox to toggle its state
checkbox.click()

# Wait for the dropdown menu to be clickable
dropdown = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.NAME, "sort"))
)
# Create a Select object
select = Select(dropdown)
# Select the option by its value
select.select_by_value("BY_DISCOUNT_DESCENDING")

# Wait for the product elements to load
WebDriverWait(driver, 5).until(
    EC.visibility_of_all_elements_located((By.CLASS_NAME, "DealGridItem-module__dealItemContent_1vFddcq1F8pUxM8dd9FW32"))
)

# Find all product elements on the page
product_elements = driver.find_elements(By.CLASS_NAME, "DealGridItem-module__dealItemContent_1vFddcq1F8pUxM8dd9FW32")

# Iterate over each product element to extract the product name and URL
for product_element in product_elements:
    # Extract product name
    product_name_element = product_element.find_element(By.CLASS_NAME, "DealContent-module__truncate_sWbxETx42ZPStTc9jwySW")
    product_name = product_name_element.text

    # Extract product URL
    product_url_element = product_element.find_element(By.CSS_SELECTOR, "a.DealCard-module__linkOutlineOffset_2fc037WfeGSjbFp1CAhOUn")
    product_url = product_url_element.get_attribute("href")

    # Print the scraped product name and URL
    print("Product Name:", product_name)
    print("Product URL:", product_url)
    print()

# Close the WebDriver
driver.quit()






