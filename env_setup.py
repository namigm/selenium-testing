import os
from dotenv import load_dotenv
load_dotenv()

BASE_URL = os.getenv('BASE_URL')
CHECK_VALIDATE_URL = f"{BASE_URL}/check_and_validate.html"
INPUT_CLICK_URL = f"{BASE_URL}/input-and-click.html"






