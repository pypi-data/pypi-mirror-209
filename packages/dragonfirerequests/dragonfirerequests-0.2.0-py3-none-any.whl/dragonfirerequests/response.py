from requests import Response, PreparedRequest


class DragonResponse:
    origin: Response
    data: dict
    success: bool
    request: PreparedRequest

    def __init__(self, response: Response, data: dict, success: bool, request: PreparedRequest):
        self.origin = response
        self.data = data
        self.success = success
        self.request = request
