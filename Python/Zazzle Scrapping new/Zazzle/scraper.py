import scrapy
from scrapy.crawler import CrawlerProcess
import undetected_chromedriver as uc
from scrapy.http import HtmlResponse
import re

# ====================================================================================================
# PROJECT SETTINGS
# ====================================================================================================

SETTINGS = {
    'ROBOTSTXT_OBEY': False,
    'REQUEST_FINGERPRINTER_IMPLEMENTATION': "2.7",
    'TWISTED_REACTOR': "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
    'FEED_EXPORT_ENCODING': "utf-8",
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    
    # === PROXY SETTINGS ===
    # You MUST replace this with a real residential proxy URL
    # Format: 'http://user:password@proxy_server:port'
    'PROXY_URL': 'http://user:password@residential_proxy.com:8080',
    'DOWNLOADER_MIDDLEWARES': {
        'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 400,
    }
}

# ====================================================================================================
# SPIDER CODE
# ====================================================================================================
class ZazzleSpider(scrapy.Spider):
    name = 'zazzle_products'
    
    def start_requests(self):
        url = 'https://www.zazzle.com/simple_black_white_overlay_photo_wedding_invitation-256139245543951273'
        
        # Initialize undetected-chromedriver with proxy
        options = uc.ChromeOptions()
        options.add_argument('--headless')
        # Add the proxy argument to ChromeOptions
        options.add_argument(f'--proxy-server={SETTINGS["PROXY_URL"]}')
        
        driver = uc.Chrome(options=options)
        
        try:
            driver.get(url)
            
            # Scrape the content after the page has fully loaded
            response = HtmlResponse(url=driver.current_url, body=driver.page_source, encoding='utf-8')
            
            # Check for bot detection page
            if "Access to this page has been denied" in response.text:
                self.logger.info("Bot detected. Access denied.")
            else:
                yield from self.parse_product(response)
        
        finally:
            driver.quit()

    def parse_product(self, response):
        # Title
        title_element = response.css('h1[class*="ProductSpaceDetailsPod_title"]::text').get()
        title = title_element.strip() if title_element else 'N/A'
        
        # Price
        price_element = response.css('div[class*="Pricing_mainPrice"]::text').get()
        price = price_element.strip() if price_element else 'N/A'
        
        # Description
        desc_element = response.css('div[class*="SeeMore_content"] div::text').get()
        description = desc_element.strip() if desc_element else 'N/A'

        # View Count
        view_count = 'N/A'
        view_text = response.xpath("//div[contains(text(), 'people viewed this design')]/text()").get()
        if view_text:
            match = re.search(r'([\d\.]+[Kk])', view_text)
            if match:
                view_count = match.group(1)
        
        # Created On
        created_on = 'N/A'
        created_on_text = response.xpath("//div[contains(text(), 'Created on:')]/span/text()").get()
        if created_on_text:
            created_on = created_on_text.strip()
            
        # Tags
        tags = response.css('div[class*="Tags-tagsList"] span::text').getall()
        tags_string = ', '.join(tags) if tags else 'N/A'
            
        yield {
            'Title': title,
            'Price': price,
            'Description': description,
            'View Count': view_count,
            'Created On': created_on,
            'Tags': tags_string,
            'URL': response.url,
        }

# ====================================================================================================
# RUN SCRIPT
# ====================================================================================================
if __name__ == '__main__':
    process = CrawlerProcess(SETTINGS)
    process.crawl(ZazzleSpider)
    process.start()
