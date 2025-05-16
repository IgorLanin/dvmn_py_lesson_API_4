import requests
from pathlib import Path
import os
from dotenv import load_dotenv
from get_img_extention import get_img_extention
from download_images import download_image


def fetch_nasa_apod(token):
    nasa_apod_api = "https://api.nasa.gov/planetary/apod"
    imgs_number = 30
    payload = {
        "api_key": token,
        "count": imgs_number
    }

    response = requests.get(nasa_apod_api, params=payload)
    response.raise_for_status()

    api_response = response.json()

    links = [link.get('url') for link in api_response]

    for link_number, link in enumerate(links, start=1):
        img_extention = get_img_extention(link)
        if not img_extention:
            continue

        nasa_apod_filename = f'images/nasa_apod_{link_number}{img_extention}'

        download_image(link, nasa_apod_filename)


def main():
    Path('images').mkdir(parents=True, exist_ok=True)

    load_dotenv()
    nasa_api_token = os.getenv("NASA_API_KEY", default=None)

    fetch_nasa_apod(nasa_api_token)


if __name__ == '__main__':
    main()
