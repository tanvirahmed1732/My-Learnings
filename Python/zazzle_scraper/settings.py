# Scrapy settings for zazzle_scraper project
BOT_NAME = "zazzle_scraper"
SPIDER_MODULES = ['zazzle_scraper.spiders']
NEWSPIDER_MODULE = 'zazzle_scraper.spiders'

# Obey robots.txt rules
ROBOTS_TXT_OBEY = False

# Configure downloader middlewares to use Selenium
DOWNLOADER_MIDDLEWARES = {
    'scrapy_selenium.SeleniumMiddleware': 800,
}

# Configure Selenium to use your chromedriver
SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = 'C:/Users/Tanvir Ahmed/AppData/Roaming/undetected_chromedriver/undetected_chromedriver.exe'
SELENIUM_DRIVER_ARGUMENTS = ['--headless']

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"