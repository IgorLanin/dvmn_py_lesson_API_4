import requests
from pathlib import Path
import os
from dotenv import load_dotenv
import datetime
from download_images import download_image


def fetch_nasa_epic(token):
    nasa_epic_api = "https://api.nasa.gov/EPIC/api/natural"
    payload = {
        "api_key": token
    }

    response = requests.get(nasa_epic_api, params=payload)
    response.raise_for_status()

    last_five_slices = 5
    api_response = response.json()[:last_five_slices]

    links = []
    for each_epic in api_response:
        nasa_epic_date = datetime.datetime.fromisoformat(each_epic['date']).strftime("%Y/%m/%d")
        nasa_epic_name = each_epic['image']
        nasa_epic_url = f"https://api.nasa.gov/EPIC/archive/natural/{nasa_epic_date}/png/{nasa_epic_name}.png"

        links.append(nasa_epic_url)

    for link_number, link in enumerate(links, start=1):
        nasa_epic_filename = f'images/nasa_epic_{link_number}.png'

        download_image(link, nasa_epic_filename, payload=payload)


def main():
    Path('images').mkdir(parents=True, exist_ok=True)

    load_dotenv()
    nasa_api_token = os.getenv("NASA_API_KEY", default=None)

    fetch_nasa_epic(nasa_api_token)


if __name__ == '__main__':
    main()
