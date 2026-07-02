from repositories import product_repository


def get_all_products():
    return product_repository.find_all()


def get_product_by_id(product_id):
    return product_repository.find_by_id(product_id)


def create_product(name, price):
    return product_repository.save(name, price)


def update_product(product_id, name, price):
    product_repository.update(product_id, name, price)


def delete_product(product_id):
    product_repository.delete(product_id)