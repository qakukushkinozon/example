import os
from dotenv import load_dotenv

load_dotenv()

class Headers:

    basic = {
        "Authorization": f"Bearer {os.getenv('ACCESS_TOKEN')}",
        "x-Task-Id": "API-1"
    }