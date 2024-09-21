from selenium import webdriver
from selenium.webdriver.common.by import By

# Setup WebDriver
driver = webdriver.Chrome()
driver.get('https://store.google.com/IN/?utm_source=hp_header&utm_medium=google_ooo&utm_campaign=GS100042&hl=en-GB')

try:
    # Locate the element
    element = driver.find_element(By.XPATH, '//*[@id="Pixel_9_Family_Hero"]/div/div[1]/div/div[1]/bento-budou')
    element_text = element.text

    # Print the text
    print("Extracted text:", element_text)

    # Expected text
    expected_text = "Oh hi, Gemini."

    # Locate the element
    element = driver.find_element(By.XPATH, '//*[@id="Pixel_9_Family_Hero"]/div/div[1]/div/div[2]')
    element_text = element.text

    # Print the text
    print("Extracted text:", element_text)

    # Expected text
    expected_text = """Meet the new Pixel 9 Pro XL, Pixel 9 Pro, Pixel 9, and Pixel 9 Pro Fold with Gemini.

(Stock subject to availability with the retailer)"""

    # Assertion with pass/fail output
    if element_text == expected_text:
        print("Test Passed: The text matches the expected value.")
    else:
        print("Test Failed: Expected '{}' but got '{}'.".format(expected_text, element_text))

except Exception as e:
    print("An error occurred:", e)
finally:
    driver.quit()  # Ensure the browser is closed


