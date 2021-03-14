import requests

class RateLimitError(Exception):

    def __init__(self, token, status_code: int = 429, message: str = "You have been rate limited, please try again later in {} seconds"):
        self.status_code = status_code
        self.message = message
        self.message = self.message.format((requests.get("https://api.bytestobits.dev/info/", headers={'Authorization': token}).json())['next_reset'])
        super().__init__()

    def __str__(self):
        return f'{self.status_code}: {self.message}'
