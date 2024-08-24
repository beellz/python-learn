# learning to calls api and get response from them

import requests # type: ignore
import json



def get_data_from_api(url, params=None):
    """
    Makes a GET request to the specified API URL with optional parameters.

    :param url: The API endpoint URL.
    :param params: A dictionary of query parameters to include in the request.
    :return: The JSON response from the API if the request is successful, otherwise None.
    """
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        return response.json()  # Return the JSON content of the response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
api_url = "https://catfact.ninja/breeds"
# parameters = {"key1": "value1", "key2": "value2"}
data = get_data_from_api(api_url)
print(data)
# facts = data.get('fact')

# for i in range(1):
#     api_url = "https://catfact.ninja/breeds"
#     # parameters = {"key1": "value1", "key2": "value2"}
#     data = get_data_from_api(api_url)
#     # facts = data.get('fact')
#     print(data)


import json
with open('data.json', 'w') as f:
    json.dump(data, f)



