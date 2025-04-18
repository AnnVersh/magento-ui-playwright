def test_header_title(sale_page):
    sale_page.open_page()
    sale_page.check_page_header_title_is('Sale')


def test_womens_sales_link(sale_page):
    sale_page.open_page()
    sale_page.check_link_text_womens_sale_is_correct(
        'Shop Women’s Deals'
    )


def test_mens_sales_link(sale_page):
    sale_page.open_page()
    sale_page.check_link_text_mens_sale_is_correct(
        'Shop Men’s Deals'
    )


def test_20_percent_discount_text(sale_page):
    sale_page.open_page()
    sale_page.check_discount_20_is(
        '20% OFF'
    )
