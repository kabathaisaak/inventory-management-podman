class ResourceNotFoundError(Exception):
    """
    Raised when a requested resource cannot be found.
    """

    def __init__(self, resource, resource_id):
        self.resource = resource
        self.resource_id = resource_id
        self.message = f"{resource} with ID {resource_id} not found."
        super().__init__(self.message)