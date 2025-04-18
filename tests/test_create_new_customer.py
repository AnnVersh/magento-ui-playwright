def test_create_new_account_valid_data(create_new_customer_page):
    create_new_customer_page.open_page()
    create_new_customer_page.fill_and_submit_valid_form('Qwerty1235!AB')


def test_password_confirmation_error(create_new_customer_page):
    create_new_customer_page.open_page()
    create_new_customer_page.check_not_matching_passwords_error(
        'Qwerty1235!A',
        'Qwerty1235!AB'
    )


def test_invalid_email_error(create_new_customer_page):
    create_new_customer_page.open_page()
    create_new_customer_page.check_invalid_email_error('yywejsjd')
