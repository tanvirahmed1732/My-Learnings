import re
import time
import pandas as pd
from playwright.sync_api import sync_playwright

IN_CSV  = r"D:\Code\GitHub\My-Learnings\zazzle\zazzle_products_to_fill.csv"
OUT_CSV = r"D:\Code\GitHub\My-Learnings\zazzle\zazzle_products_filled.csv"

CREATED_RE = re.compile(r"Created on:\s*([0-9]{1,2}/[0-9]{1,2}/[0-9]{4},\s*[0-9]{1,2}:[0-9]{2}\s*[AP]M)", re.I)
VIEWS_RE   = re.compile(r"(?:Views|Viewed)\s*(?:on|:)?\s*([0-9][0-9,]*)", re.I)

def extract_from_text(page_text: str):
    created = ""
    views = ""
    tags = ""

    m = CREATED_RE.search(page_text)
    if m:
        created = m.group(1).strip()

    mv = VIEWS_RE.search(page_text)
    if mv:
        views = mv.group(1).replace(",", "").strip()

    # Tags section: find "Tags" line then take following non-empty lines
    lines = [ln.strip() for ln in page_text.splitlines() if ln.strip()]
    for i, ln in enumerate(lines):
        if ln.lower() == "tags":
            # Typically next line might be category then a long tag line
            block = lines[i+1:i+6]
            if block:
                best = max(block, key=lambda s: len(s))
                # On Zazzle these are usually space-separated tags. Convert to comma-separated.
                tags = ", ".join(best.split())
            break

    return created, views, tags

def main():
    df = pd.read_csv(IN_CSV)
    created_list, views_list, tags_list = [], [], []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36",
            locale="en-US",
        )
        page = context.new_page()

        for idx, row in df.iterrows():
            url = str(row["link"]).strip()
            created = views = tags = ""

            try:
                page.goto(url, wait_until="domcontentloaded", timeout=60000)
                page.wait_for_timeout(1500)  # allow page content to settle
                text = page.inner_text("body")
                created, views, tags = extract_from_text(text)
            except Exception as e:
                print(f"Failed: {url} ({e})")

            created_list.append(created)
            views_list.append(views)
            tags_list.append(tags)

            time.sleep(1.0)

        browser.close()

    df["created_on"] = created_list
    df["views"] = views_list
    df["tags"] = tags_list
    df.to_csv(OUT_CSV, index=False)
    print(f"Saved: {OUT_CSV}")

if __name__ == "__main__":
    main()
