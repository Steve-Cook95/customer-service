from customer_service.model.customer import Customer


def get_customer(customer_id, customer_repository):
    return customer_repository.fetch_by_id(customer_id)


def create_customer(first_name, surname, customer_repository):
    customer = Customer(first_name=first_name, surname=surname)
    customer_repository.store(customer)

    return customer.customer_id


def update_customer(customer_id, first_name, surname, customer_repository):
    customer = Customer(
        customer_id=customer_id,
        first_name=first_name,
        surname=surname)
    customer_repository.update_customer(customer)
    return customer
