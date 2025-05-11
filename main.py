import requests
from pathlib import Path
import os
from dotenv import load_dotenv
from urllib.parse import unquote, urlsplit
import datetime


def get_img_extention(link):
    parsed_link = urlsplit(link)

    unquoted_path = unquote(parsed_link[2])

    img_name = os.path.split(unquoted_path)[1]

    img_extention = os.path.splitext(img_name)[1]

    return img_extention


def fetch_spacex_last_launch(url):
    response = requests.get(url)
    response.raise_for_status()

    response_data = response.json()

    links = response_data["links"]["flickr"]["original"]
    spacex_filename = 'images/spacex{}.jpg'

    for link_number, link in enumerate(links, start=1):
        response = requests.get(link)
        response.raise_for_status()

        with open(spacex_filename.format(link_number), 'wb') as file:
            file.write(response.content)


def fetch_nasa_apod(url, token):
    payload = {
        "api_key": token,
        "count": 30
    }

    response = requests.get(url, params=payload)
    response.raise_for_status()

    response_data = response.json()

    links = []
    for link in response_data:
        links.append(link['url'])

    nasa_apod_filename = 'images/nasa_apod_{n}{extention}'

    for link_number, link in enumerate(links, start=1):
        img_extention = get_img_extention(link)

        response = requests.get(link)
        response.raise_for_status()

        with open(nasa_apod_filename.format(extention=img_extention, n=link_number), 'wb') as file:
            file.write(response.content)


def fetch_nasa_epic(url, token):
    payload = {
        "api_key": token
    }

    response = requests.get(url, params=payload)
    response.raise_for_status()

    response_data = response.json()[:5]

    links = []
    for each_epic in response_data:
        nasa_epic_date = datetime.datetime.fromisoformat(each_epic['date']).strftime("%Y/%m/%d")
        nasa_epic_name = each_epic['image']
        nasa_epic_url = f"https://api.nasa.gov/EPIC/archive/natural/{nasa_epic_date}/png/{nasa_epic_name}.png"

        links.append(nasa_epic_url)

    nasa_epic_filename = 'images/nasa_epic_{}.png'

    for link_number, link in enumerate(links, start=1):
        response_epic = requests.get(link, params=payload)
        response_epic.raise_for_status()

        with open(nasa_epic_filename.format(link_number), 'wb') as file:
            file.write(response_epic.content)


def main():
    Path('images').mkdir(parents=True, exist_ok=True)
    spacex_url = "https://api.spacexdata.com/v5/launches/5eb87ce4ffd86e000604b337"
    fetch_spacex_last_launch(spacex_url)

    load_dotenv()
    nasa_api_token = os.getenv("NASA_API_KEY", default=None)
    nasa_apod_url = "https://api.nasa.gov/planetary/apod"
    fetch_nasa_apod(nasa_apod_url, nasa_api_token)

    nasa_epic_url = "https://api.nasa.gov/EPIC/api/natural"
    fetch_nasa_epic(nasa_epic_url, nasa_api_token)


if __name__ == '__main__':
    main()
