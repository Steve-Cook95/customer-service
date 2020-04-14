from behave import when, given


@given('customer "{name}" with ID "{customer_id:d}" exists')
def find_customer(context, name, customer_id):
    (first_name, surname) = name.split(' ', 2)

    # find customer in the database
    context.response = context.web_client.get(f'/customers/{customer_id}')


@when('I change customer with ID "{customer_id}" name to "{name}"')
def update_customer_name(context, customer_id, name):
    # change name of customer in customer DB
    (first_name, surname) = name.split(' ', 2)
    context.response = context.web_client.put(
        f'/customers/{customer_id}/{first_name}/{surname}')
