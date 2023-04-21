"""Customers at Hackbright."""


class Customer:
    """Ubermelon customer."""

    # TODO: need to implement this
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        return (
            f'<Customer: {self.first_name, self.last_name}, {self.email}>'
        )


def read_customers_from_file(filepath):
    customers = {}

    with open(filepath) as lists:
        for line in lists:
            (
                first_name,
                last_name,
                email,
                password
            ) = line.strip().split('|')

            customers[email] = Customer(
                first_name,
                last_name,
                email,
                password
            )

    return customers


def get_by_email(email):
    if email not in customers:
        return None
    else:
        return customers[email]


customers = read_customers_from_file('customers.txt')
