def test_incorrect_login(customer_login_page):
    customer_login_page.open_page()
    customer_login_page.fill_in_login_form('gjiifj@gmail.com', 'usdvh5')
    customer_login_page.check_error_alert_text_is(
        'The account sign-in was incorrect or your account '
        'is disabled temporarily. Please wait and try again later.'
    )


def test_correct_email_with_incorrect_pass(customer_login_page):
    customer_login_page.open_page()
    customer_login_page.fill_in_login_form(
        'exist@email.com',
        'non-existing-pass'
    )
    customer_login_page.check_error_alert_text_is(
        'The account sign-in was incorrect or your account '
        'is disabled temporarily. Please wait and try again later.'
    )
