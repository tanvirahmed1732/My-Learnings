import scrapy
from scrapy_selenium import SeleniumRequest
import re

class ZazzleSpider(scrapy.Spider):
    name = 'zazzle_products'
    
    def start_requests(self):
        url = 'https://www.zazzle.com/simple_black_white_overlay_photo_wedding_invitation-256139245543951273'
        yield SeleniumRequest(
            url=url,
            callback=self.parse_product,
            wait_time=5,  # Wait 5 seconds for JavaScript to load
        )

    def parse_product(self, response):
        # The 'response' object is a SeleniumResponse with the fully rendered HTML
        
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