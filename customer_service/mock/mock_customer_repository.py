from customer_service.model.errors import CustomerNotFound


class MockCustomerRepository:
    def __init__(self):
        self.customers = {}
        self.last_id = 0

    def store(self, customer):
        if customer.customer_id is None:
            self.last_id = self.last_id + 1
            customer.customer_id = self.last_id

        self.customers[customer.customer_id] = customer

    def fetch_by_id(self, id):
        # print(type(id))
        # print(self.customers)
        if id not in self.customers:
            # print("hi")
            raise CustomerNotFound()

        return self.customers[id]

    def update_customer(self, customer):
        print(customer)
        customer_object = self.fetch_by_id(int(customer.customer_id))
        print(customer_object)
        customer_object.first_name = customer.first_name
        customer_object.surname = customer.surname
        self.store(customer_object)
