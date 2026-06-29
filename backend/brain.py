from backend.router import route


def get_response(message):
    """
    Main entry point for Project F.
    """

    return route(message)