import requests
from pathlib import Path
import os
from dotenv import load_dotenv
from urllib.parse import unquote, urlsplit
import datetime
from get_img_extention import get_img_extention
from fetch_nasa_apod_images import fetch_nasa_apod
from fetch_nasa_epic_images import fetch_nasa_epic
from fetch_spacex_images import fetch_spacex_last_launch


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
