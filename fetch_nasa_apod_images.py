import requests
from pathlib import Path
import os
from dotenv import load_dotenv
from get_img_extention import get_img_extention


def fetch_nasa_apod(url, token):
    num_of_imgs = 30
    payload = {
        "api_key": token,
        "count": num_of_imgs
    }

    response = requests.get(url, params=payload)
    response.raise_for_status()

    api_response = response.json()

    links = []
    for link in api_response:
        links.append(link.get('url'))

    nasa_apod_filename = 'images/nasa_apod_{n}{extention}'

    for link_number, link in enumerate(links, start=1):
        img_extention = get_img_extention(link)
        if not img_extention:
            continue

        response = requests.get(link)
        response.raise_for_status()

        with open(nasa_apod_filename.format(extention=img_extention, n=link_number), 'wb') as file:
            file.write(response.content)


def main():
    Path('images').mkdir(parents=True, exist_ok=True)

    load_dotenv()
    nasa_api_token = os.getenv("NASA_API_KEY", default=None)
    nasa_apod_url = "https://api.nasa.gov/planetary/apod"
    fetch_nasa_apod(nasa_apod_url, nasa_api_token)


if __name__ == '__main__':
    main()
