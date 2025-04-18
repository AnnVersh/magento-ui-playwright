from faker import Faker

fake = Faker()


def generate_random_email():
    return fake.email()


def generate_random_first_name():
    return fake.first_name()


def generate_random_last_name():
    return fake.last_name()
