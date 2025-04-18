"""Using locators: '#' - id, '.' - class
"""
header_title_loc = 'h1'
womens_deals_loc = '.more.button'
mens_deals_loc = (
    '//a[@class="block-promo sale-mens"]'
    '//span[contains(@class, "more") and text()="Shop Men’s Deals"]'
)
discount_20_off = (
    '//a[@class="block-promo sale-20-off"]'
    '//strong[contains(@class, "title") and text()="20% OFF"]'
)
