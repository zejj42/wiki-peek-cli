import requests


def fetch(url, params=None, fetchType="data"):
    try:
        print(f"Fetching {fetchType}...")
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        return None
