import requests
from pathlib import Path
import os
from dotenv import load_dotenv
import datetime
from get_img_extention import get_img_extention


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

    load_dotenv()
    nasa_api_token = os.getenv("NASA_API_KEY", default=None)
    nasa_epic_url = "https://api.nasa.gov/EPIC/api/natural"

    fetch_nasa_epic(nasa_epic_url, nasa_api_token)


if __name__ == '__main__':
    main()
