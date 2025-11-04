from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# === SETTINGS ===
CHROMEDRIVER_PATH = r"D:\Download\chromedriver-win64\chromedriver.exe"  # path to your ChromeDriver

# --- Correctly load your Profile 2 ---
# Point to the main User Data directory, not directly to Profile 2
USER_DATA_DIR = r"C:\Users\Tanvir Ahmed\AppData\Local\Google\Chrome\User Data\Profile 2"
PROFILE_NAME = "Profile 2"  # exactly as your folder name

URL = "https://www.zazzle.com/simple_black_white_overlay_photo_wedding_invitation-256139245543951273"

# === CHROME OPTIONS ===
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")


# Attach to your real Chrome profile
chrome_options.add_argument(f"--user-data-dir={USER_DATA_DIR}")
chrome_options.add_argument(f"--profile-directory={PROFILE_NAME}")

# Optional: sometimes helps with DevToolsActivePort issues
chrome_options.add_argument("--remote-debugging-port=9222")

service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=chrome_options)

# === OPEN PAGE ===
driver.get(URL)
print("Browser opened using your real Chrome profile. Solve any captcha if prompted.")

# Simulate small human actions to reduce detection
time.sleep(3)
driver.execute_script("window.scrollTo(0, 400);")
time.sleep(2)
driver.execute_script("window.scrollTo(0, 800);")
time.sleep(2)

# Wait until the product title <h1> appears
try:
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'h1'))
    )
except:
    print("Warning: product title not found within timeout")

# === SAVE RENDERED HTML ===
html = driver.page_source
with open("zazzle_rendered.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Saved rendered HTML to zazzle_rendered.html")

# === PARSE WITH BEAUTIFULSOUP ===
soup = BeautifulSoup(html, "html.parser")

title = soup.select_one('h1')
price = soup.select_one('[data-testid="ProductPrice"]')
description = soup.select_one('[data-testid="AboutThisDesign"]')

# Example for tags/created on — adjust after inspecting zazzle_rendered.html
tags_container = soup.select_one('div[data-testid="TagList"]')
created_on = soup.select_one('span[data-testid="CreatedOn"]')

tags = None
if tags_container:
    tags = [t.get_text(strip=True) for t in tags_container.find_all('a')] or \
           [line.strip() for line in tags_container.get_text("\n").split("\n") if line.strip()]

print("\n--- Extracted Data ---")
print("Title:", title.get_text(strip=True) if title else None)
print("Price:", price.get_text(strip=True) if price else None)
print("Description:", description.get_text(strip=True) if description else None)
print("Tags:", tags)
print("Created On:", created_on.get_text(strip=True) if created_on else None)

driver.quit()
