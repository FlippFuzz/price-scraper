from playwright.sync_api import sync_playwright, Browser


def scrap_price(browser: Browser, url: str) -> str:
    """Scrapes the price from a given product page URL.

    This function uses an existing browser instance to create a new page,
    navigates to the specified URL, and extracts the price of a product based on
    a predefined CSS selector.

    Args:
        browser: An active Playwright browser instance.
        url: The URL of the product page to scrape.

    Returns:
        The price of the product as a string, with currency symbols and
        whitespace removed.
    """
    # Create a new page (like a browser tab).
    page = browser.new_page()
    try:
        # Navigate to the specified URL.
        page.goto(url)

        # Wait for page to load, then find the price
        # Example 1 - Result is 1.95
        # <div class="product-price-tag"><div class="font-2xl">$1.95</div></div>
        # Example 2 - Result is 1.75
        # <div class="product-price-tag"><div><span class="promo-price font-2xl">$1.75</span> <strike class="previous-price">$2.35</strike></div></div>

        # Define the CSS selector for the element containing the price.
        price_selector = (
            ".product-price-tag span.font-2xl, .product-price-tag div.font-2xl"
        )
        # Locate the element on the page.
        price_element = page.locator(price_selector)
        # Wait for the element to be available and attached to the DOM.
        price_element.wait_for()
        # Extract the text content from the located element.
        price_text = price_element.inner_text()
        # Clean the extracted text by removing the dollar sign and stripping whitespace.
        return price_text.replace("$", "").strip()
    finally:
        # Close the page to free up system resources.
        page.close()


if __name__ == "__main__":
    # This block serves as an example of how to use the scrap_price function.
    # It will only run when the script is executed directly.
    urls = [
        "https://shengsiong.com.sg/product/malaysia-long-bean-250-g-3024024",
        "https://shengsiong.com.sg/product/authentic-tea-house-oolong-chinese-tea-drink-15-l",
    ]

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        # Loop through the list of URLs to scrape.
        for url in urls:
            print(f"Working on {url}... ")
            # Call the scraper function to get the price, then print it
            price = scrap_price(browser, url)
            print(f"  {price}")
        browser.close()
