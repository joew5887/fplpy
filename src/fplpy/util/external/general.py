import time
import requests

def safe_request(url: str, retries: int = 5) -> requests.Response:
    for i in range(retries):
        response = requests.get(url)
        if response.status_code == 429:
            wait = int(response.headers.get("Retry-After", 2 ** i))
            print(f"Rate limited. Waiting {wait}s...")
            time.sleep(wait)
        else:
            return response

    raise Exception("Max retries exceeded")