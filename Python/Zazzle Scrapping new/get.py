from bs4 import BeautifulSoup

with open("a.html", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

title = soup.select_one('h1')
price = soup.select_one('#main > div:nth-child(1) > div.WwwPage_root > div > div.WwwPage_shieldWrapper > main > div > div.GAContext-CMSPage.PdpCms-cmsContent > section.row.CmsSectionPdp.CmsSectionPdp-section1897085.sectionType--pdpProductSpace > div > div > div > div > div.ProductSpace-main > div.ProductSpace-detailsWrapper > div > div > div.Attributes-level1 > div.Attributes-details > div.ProductSpaceDetailsPod_root > div.ProductSpaceDetailsPod_pricing > div.Pricing_root > div.Pricing_mainPriceContainer > div.Pricing_mainPrice')
description = soup.select_one('#main > div:nth-child(1) > div.WwwPage_root > div > div.WwwPage_shieldWrapper > main > div > div.GAContext-CMSPage.PdpCms-cmsContent > section.row.CmsSectionPdp.CmsSectionPdp-section1897099.sectionType--pdpAboutProductAboutDesign > div > div > div:nth-child(2) > div.AboutThisDesign.row > div.large-8.pull-4.small-12.column > div.SeeMore_root > div > div > div')
datee=soup.select_one('#main > div:nth-child(1) > div.WwwPage_root > div > div.WwwPage_shieldWrapper > main > div > div.GAContext-CMSPage.PdpCms-cmsContent > section.row.CmsSectionPdp.CmsSectionPdp-section1897108.sectionType--pdpTagsOtherInfo > div > div > div:nth-child(2) > div.OtherInfo > div:nth-child(2) > span')


print("Title:", title.get_text(strip=True) if title else None)
print("Price:", price.get_text(strip=True) if price else None)
print("Description:", description.get_text(strip=True) if description else None)
print("Created on date:", datee.get_text(strip=True) if datee else None)
