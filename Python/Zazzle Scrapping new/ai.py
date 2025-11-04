from scrapegraph_py import Client
from scrapegraph_py.logger import sgai_logger
from pydantic import BaseModel
from typing import List, Optional

sgai_logger.set_logging(level="INFO")

# Define the output schema as a Pydantic BaseModel subclass
class ProductSchema(BaseModel):
    product_title: str
    price: str
    description: str
    views: Optional[str] = None
    tags: Optional[List[str]] = None
    created_on_date: Optional[str] = None

# Initialize the client with your API key
client = Client(api_key="sgai-f0d17530-5fb1-4dbd-a7a0-df21a486a04f")

# First request without schema
response = client.smartscraper(
    website_url="https://www.zazzle.com/simple_black_white_overlay_photo_wedding_invitation-256139245543951273",
    user_prompt=(
        "Extract the product title, price, description, number of views (if available), "
        "tags as a list, and creation date from the page."
    )
)

# Second request with schema
response_with_schema = client.smartscraper(
    website_url="https://www.zazzle.com/simple_black_white_overlay_photo_wedding_invitation-256139245543951273",
    user_prompt=(
        "Extract the following fields from the product page: "
        "product_title, price, description, views (if available), tags (list), created_on_date. "
        "Return only these fields following the schema."
    ),
    output_schema=ProductSchema  # <- pass the class here
)

client.close()

print(response)
print(response_with_schema)
