from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import json
import os

DIR = os.path.dirname(os.path.abspath(__file__))

# ---- basic selenium usage ----

# open browser and visit a page
driver = webdriver.Chrome()
driver.get("https://example.com")

print(driver.title)
print(driver.current_url)


# find element by id
# driver.find_element(By.ID, "search")

# find element by class name
# driver.find_element(By.CLASS_NAME, "product")

# find element by css selector
# driver.find_element(By.CSS_SELECTOR, ".product")

# find element by tag name
# driver.find_element(By.TAG_NAME, "h1")

# find multiple elements
# driver.find_elements(By.CLASS_NAME, "item")


# get text from element
h1 = driver.find_element(By.TAG_NAME, "h1")
print(h1.text)


# get attribute (like href, src)
link = driver.find_element(By.TAG_NAME, "a")
print(link.text)
print(link.get_attribute("href"))


driver.quit()


# ---- click and type example ----

driver = webdriver.Chrome()
driver.get("https://www.google.com")

# find search box and type
search = driver.find_element(By.NAME, "q")
search.send_keys("python web scraping")
search.send_keys(Keys.RETURN)

# wait for results to load
time.sleep(2)

# get all result titles
results = driver.find_elements(By.CSS_SELECTOR, "h3")
for r in results[:5]:
    print(r.text)

driver.quit()


# ---- explicit waits (better than time.sleep) ----

driver = webdriver.Chrome()
driver.get("https://example.com")

# wait up to 10 seconds until element is present
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )
    print(element.text)
except Exception as e:
    print("element not found:", e)

driver.quit()


# ---- scrolling ----

driver = webdriver.Chrome()
driver.get("https://example.com")

# scroll to bottom of page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)

# scroll back to top
driver.execute_script("window.scrollTo(0, 0);")

driver.quit()


# ---- scraping dynamic content ----

driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com/js/")

# wait for quotes to load (javascript-rendered)
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "quote"))
    )

    quotes = driver.find_elements(By.CLASS_NAME, "quote")
    data = []

    for q in quotes:
        text = q.find_element(By.CLASS_NAME, "text").text
        author = q.find_element(By.CLASS_NAME, "author").text
        data.append({"quote": text, "author": author})
        print(author, "->", text[:50])

    with open(os.path.join(DIR, "quotes.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print("saved to quotes.json")

except Exception as e:
    print("error:", e)

finally:
    driver.quit()
