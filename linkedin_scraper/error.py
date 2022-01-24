class AuthenticationError(Exception):
    """Unable to login to LinkedIn"""

    def __init__(self, message="Unable to login to LinkedIn"):
        self.message = message
        super().__init__(self.message)

class HTMLError(Exception):
    """Unable to complete HTML requests"""
    def __init__(self, message="Cannot complete HTML requests. Unknown Error"):
        self.message = message
        super().__init__(self.message)

class NoConnectionsError(Exception):
    """No connections found"""
    def __init__(self, message="No connections found"):
        self.message = message
        super().__init__(self.message)