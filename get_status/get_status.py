
import requests # type: ignore
import json

def get_data_from_api(url, params=None):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        print(response.status_code)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
api_url = [ "https://jellyfin.beellz.com" , "https://kindle.beellz.com" , "https://google.com", "https://torrent.beellz.com"]


for i in api_url:
    print(i)
    data = get_data_from_api(i)


