import requests
from dataclasses import dataclass
from dotenv import load_dotenv
load_dotenv() # Just incase.

global __version__
__version__ = "1.0.0"
global __endpoint__
__endpoint__ = "https://api.bracelet.oriaxen.com"

@dataclass
class BraceletData:
    status: str
    user: dict
    kv: dict

class Bracelet():
    """The Bracelet Object is created/registred from here to save your config."""
    def __init__(self, endpoint: str | None = "https://api.bracelet.oriaxen.com", debug: bool = False):
        self.endpoint = endpoint
        __endpoint__ = endpoint
        self.debug = debug

    def fetch_data(self, UserID):
        if not (UserID and self and self.debug and self.endpoint):
            return None # I will eventually handle this properly.
        if self.debug == True:
            print(f"[Bracelet] Fetching BraceletData for {UserID} using {self.endpoint}")
        sub = True if self.endpoint.Startswith("api") else False
        _data = None # Again I will handle this properly eventually.
        try:
            _data = requests.get(f'{self.endpoint}/v1/users/{self.UserID}' if sub == True else '{self.endpoint}/api/v1/users/{UserID}')
        except Exception as e:
            _data = None # This will be handled properly eventually.
            if self.debug == True:
                print(f"[Bracelet] An Error Occurred While Fetching The Data For {UserID}: {e}")
        return _data
