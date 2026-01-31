import re
import pandas as pd
from datetime import datetime
from dateutil import parser as dateparser

from playwright.sync_api import sync_playwright

INPUT_CSV  = r"D:\Code\GitHub\My-Learnings\Python\zazzle\Scraping - Bug.csv"
OUTPUT_CSV = r"D:\Code\GitHub\My-Learnings\Python\zazzle\Scraping - Bug Final.csv"

URL_COL = "data-page-selector"
TEXT1_COL = "text_1"

CREATED_ON_COL = "created_on"

# Your selector
CREATED_ON_SELECTOR = r"""#main > div:nth-child(1) > div.WwwPage_root > div > div.WwwPage_shieldWrapper > main > div > div.GAContext-CMSPage.PdpCms-cmsContent > section.row.CmsSectionPdp.CmsSectionPdp-section1929152.sectionType--pdpTagsOtherInfo > div > div > div > div:nth-child(2) > div.OtherInfo > div:nth-child(2) > span"""

def parse_text1_to_int(val):
    if pd.isna(val):
        return None
    s = str(val).strip()

    m = re.search(r"([\d,.]+)\s*([kKmM]?)", s)
    if not m:
        return None

    num = m.group(1).replace(",", "")
    suf = m.group(2).lower()

    try:
        f = float(num)
    except:
        return None

    mult = 1
    if suf == "k":
        mult = 1000
    elif suf == "m":
        mult = 1_000_000

    return int(round(f * mult))

def parse_created_on_text(raw_text: str):
    """
    Tries to extract a date from whatever the span contains.
    Works if the span is like:
      "Created on January 3, 2024"
      "Created: Jan 3, 2024"
      "Jan 3, 2024"
    """
    if not raw_text:
        return None

    t = raw_text.strip()
    # Remove common prefixes
    t = re.sub(r"(?i)created\s*(on)?\s*[:\-]?\s*", "", t).strip()

    try:
        dt = dateparser.parse(t, fuzzy=True)
        if dt:
            return dt.date()
    except:
        return None

    return None

df = pd.read_csv(INPUT_CSV)

# Normalize text_1
df[TEXT1_COL] = df[TEXT1_COL].apply(parse_text1_to_int)

# Prepare created_on column
if CREATED_ON_COL not in df.columns:
    df[CREATED_ON_COL] = None

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    for i, url in enumerate(df[URL_COL].astype(str).tolist()):
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            page.wait_for_selector(CREATED_ON_SELECTOR, timeout=30000)

            raw = page.locator(CREATED_ON_SELECTOR).inner_text().strip()
            created_date = parse_created_on_text(raw)

            df.at[i, CREATED_ON_COL] = created_date.isoformat() if created_date else None
            print(f"{i+1}/{len(df)} OK | {created_date} | {url}")

        except Exception as e:
            df.at[i, CREATED_ON_COL] = None
            print(f"{i+1}/{len(df)} FAIL | {e} | {url}")

    browser.close()

# Sort by created_on as actual date
df[CREATED_ON_COL] = pd.to_datetime(df[CREATED_ON_COL], errors="coerce")
df = df.sort_values(by=CREATED_ON_COL, ascending=True, na_position="last").reset_index(drop=True)

df.to_csv(OUTPUT_CSV, index=False)
print("Saved:", OUTPUT_CSV)