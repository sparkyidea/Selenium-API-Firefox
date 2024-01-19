from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def bing_search(query):
    # Path to geckodriver
    # Make sure geckodriver is in your PATH or specify the path directly
    options = FirefoxOptions()
    options.add_argument("-headless")

    driver_path = '/usr/local/bin/geckodriver'
    driver = webdriver.Firefox(service=FirefoxService(driver_path), options=options)

    try:
        # Navigate to Google
        driver.get("http://www.bing.com")

        # Locate the search box
        search_box = driver.find_element(By.XPATH, '//textarea[@type="search"]')

        # Enter the search query in the search box
        search_box.send_keys(query)
        time.sleep(3)

        # Submit the query
        search_box.send_keys(Keys.RETURN)

        # Wait for results to load
        time.sleep(3)

        # Find all search result titles
        search_results = driver.find_elements(By.XPATH, '//li/div/h2')

        # Print the text of each search result title
        
        container = []

        for search_result in search_results:
            if search_result.text:
              container.append(search_result.text)

        driver.quit()
        return container
    except Exception as e:
        driver.quit()
        return e

if __name__ == "__main__":
  # Replace 'Your Search Query' with your actual search query
  result = google_search("Your Search Query")
  print(result)
