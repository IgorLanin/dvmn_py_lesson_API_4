import requests


def download_image(get_data, filename, payload=None):
    response = requests.get(get_data, params=payload)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)